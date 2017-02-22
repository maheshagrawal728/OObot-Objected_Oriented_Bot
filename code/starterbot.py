import os
import time
from slackclient import SlackClient
import cacheit
import chatbot
import usecase1
import usecase2
import usecase3
import tempStoreRepo

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

commanddict = {"hi": "hello. How are you?"}
ongoingConversation = False
templateLink  = ""
templateName = ""
languageProg = ""
needreponame = False
needLanguage = False
currentUseCase = -1

def handle_command(command, channel):
    global templateLink
    global currentUseCase
    global needLanguage
    needTemplate = False
    global templateName
    global ongoingConversation
    global languageProg

    command = command.strip('?')
    if "exit" in command:
        ongoingConversation = False
        needTemplate = False
        currentUseCase = -1
        return
    if ongoingConversation:
        handle_OngoingConversations(command, channel)
        return
    command = command.lower()
    templateName = ""
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."

    currentUseCase = chatbot.identifyUseCase(command)
    # starts and builds the conversation
    if ("hello" in command or "hi" in command) and "again" in command:
        response = "Can't you leave me alone for few minutes"
    elif "hi" == command or "hello" in command:
        response = "hello"
    elif currentUseCase == 1:
        templateName = chatbot.getPattern(command)
        print "Requested template name is " + templateName
        needTemplate = True
    elif currentUseCase == 2:
        ongoingConversation = True
        response = "provide the pattern name, programming language, and github link seperated by comma like factory,java, https://github.com/oobot/factory\nGithub link should be from a public repo in github.com and not github.ncsu.edu"
    elif currentUseCase == 3:
        response = "provide the pattern name and preferred language to search for like factory,java"
        ongoingConversation = True
    elif "future" in command:
        response = "Thanks"
    else:
        response = "I don't understand your command. Enter again"

    if needTemplate:
        ongoingConversation = True
        if chatbot.getLanguage(command) != 'NA':
            languageProg = chatbot.getLanguage(command)
            templateLink =cacheit.useCase1(templateName, languageProg)
            availablePatterns = cacheit.getAvailPatterns()
            if (templateName+'-'+languageProg) not in availablePatterns:
                response = "The pattern does not exist"
                ongoingConversation = False
                currentUseCase = -1
            else:
                response = "Do you want to download the files or want me to upload it to a repo?"
        else:
            needLanguage = True
            response = "Please enter programming language"
    if response != "":
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

# builds the conversation to satisfy the user's intial request
def handle_OngoingConversations(command, channel):
    global templateLink
    global ongoingConversation
    global needreponame
    global currentUseCase
    global templateName
    global needLanguage
    global languageProg
    response = ""
    if currentUseCase == 1:
        if needLanguage == True:
            languageProg = chatbot.getLanguage(command)
            if languageProg == 'NA':
                response = "Not supported. Please enter different language among "+str(chatbot.getAvailableLanguages()) +" or type @oobot exit to exit conversation"
            else:
                templateLink = cacheit.useCase1(templateName, languageProg)
                availablePatterns = cacheit.getAvailPatterns()
                print availablePatterns
                if (templateName + '-' + languageProg) not in availablePatterns:
                    response = "The pattern does not exist"
                    currentUseCase = -1
                    ongoingConversation = False
                else:
                    response = "Do you want to download the files or want me to upload it to a repo?"
                needLanguage = False
        elif needreponame:
            if len(command.strip().split(',')) < 2:
                response = 'Invalid input. Enter again or give exit to stop conversation'
            else:
                reponame = command.split(",")[1].strip()
                userName = command.split(",")[0].strip()
                usecase1Result = usecase1.UseCase1(userName, reponame, templateName, languageProg)
                if(usecase1Result != -1 and usecase1Result == ""):
                    response = "The template is pushed to the specified repo with branch name oobot."
                elif(usecase1Result != -1):
                    response = "The template is pushed to the specified repo with branch name oobot. The link is: "+usecase1Result
                else:
                    response = "Sorry. An unexpected error has prevented the file upload. Please use this link to download: "+templateLink
                needreponame = False
                ongoingConversation = False
        else:
            if "yes" in command.lower() or "yeah" in command.lower() or "download" in command.lower():
                response = "The template can be downloaded from the link: "+templateLink
                ongoingConversation = False
            elif "no" in command.lower() or "clone" in command.lower() or "upload" in command.lower():
                response = "Please provide your ncsu github username, repo name seperated by comma and add me as a collaborator to the repo"
                needreponame = True
            else:
                ongoingConversation = False
                currentUseCase = -1

    elif currentUseCase == 2:
        availablePatterns = cacheit.getAvailPatterns()
        if "," not in command:
            response = "Please enter again"
        else:
            # user gives the pattern name, its language and its url in comma separated format
            templateName,languageProg,link = command.split(",")
            templateName = templateName.strip().lower()
            templateName = templateName.replace(' ', '-')
            link = link.strip()
            languageProg = languageProg.strip()
            httpLoc = link.find('http')
            link = link[httpLoc : link.find('>', httpLoc)]
            templateNameLang = templateName + '-' + languageProg
            if templateNameLang in availablePatterns:
                response = "The pattern already exists. Operation Failed"
            else:
                cacheit.useCase2(templateName, languageProg)
                usecase2Result = usecase2.UseCase2(templateName, languageProg, link)
                if( usecase2Result ==1):
                    response = "Pattern added successfully"
                else:
                    response = "Oops, something went wrong! Please try again later!"
            ongoingConversation = False
    elif currentUseCase == 3:
        if len(command.strip().split(',')) < 2:
            response = 'invalid input'
            ongoingConversation = False
        else:
            templateName, prefLang = command.strip().split(',')
            response = usecase3.UseCase3(templateName, prefLang)
        ongoingConversation = False
    if response != "":
        slack_client.api_call("chat.postMessage", channel=channel,
                        text=response, as_user=True)
    else:
	    slack_client.api_call("chat.postMessage", channel=channel,
			text="Sorry, could not find relevant results", as_user=True)

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        # clone all the repos that OOBOT has to a temp directory
        tempStoreRepo.cloneRepoFromDataStore()
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
