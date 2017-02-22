import json
from collections import defaultdict
import githubWrapper

data = defaultdict(lambda: "Sorry, pattern not found")
with open('cache.json', 'r+') as data_file:
    jsonData = json.load(data_file)
    data.update(jsonData)
    del jsonData
    # get the list of repos that OOBOT already has in its data store
    repos = githubWrapper.listOrganisationRepos('OOBOT')
    if repos != None:
        data["gitName"] = {}
        data["localpaths"] = {}
        for repo in repos:
            data["gitName"][repo["name"]] = repo["url"]
            data["localpaths"][repo["name"]] = "../OOBOT/" + repo["name"]

# identifies the appropriate usecase and redirects to it
def createGitHubMockClient():
    useCaseDict = {}
    useCaseDict[1] = useCase1
    useCaseDict[2] = useCase2
    useCaseDict[3] = useCase3
    validUseCases = set([1, 2, 3])
    while True:
        useCase = useCaseCheck()
        if useCase not in validUseCases:
            break
        # calling appropriate use case
        useCaseDict[useCase]()
        print  # just as empty print for new line


def useCaseCheck():
    print "Which use-case would you like to perform: "
    print "1: request for template code"
    print "2: provide template code"
    print "3: search for template in GitHub:"
    print "input any other number if u r done"
    useCase = ""
    while not useCase.isdigit():
        useCase = raw_input()
        if not useCase.isdigit():
            print "Please enter valid use case"
    return int(useCase)

# fetches the pattern that OOBOT has in its data store
def useCase1(pattern, lang):
    global data
    resp = ""
    try:
        gitLink = "https://github.ncsu.edu/OOBOT/"+pattern+'-'+lang + '/archive/master.zip'
    except KeyError:
        return -1
    resp += gitLink
    return resp

# upload the pattern given by the user to OOBOT's data store
def useCase2(templateName, language):
    data["gitName"][templateName+'-'+language] = "https://github.ncsu.edu/OOBOT/" + templateName+'-'+language
    updateTemplate(templateName)

# searches the specified pattern in public github repos
def useCase3(pattern):
    global data
    resp = ""
    total_count = int(data["search-repo"]["total_count"])
    if total_count == 0:
        resp += "OOPS! I dont know what that mean..."
        return
    resp += "Here is what I thought might interest you...\n"
    for i in range(0, total_count):
        if data["search-repo"]["items"][i]:
            resp += data["search-repo"]["items"][i]["html_url"]
            resp += "\n"
    return resp


def getAvailPatterns():
    return set(map(str, data["gitName"].keys()))


def getCacheData():
    return data

# pushes the list of possible ways on pattern search text into data dump
def updateTemplate(templateName):
    newEntries = allCombi(templateName)
    for k in newEntries:
        if k not in data['diffPatterns']:
            data['diffPatterns'][k] = templateName

# prepares the list of possible ways that the user can search for the pattern
def allCombi(templateName):
    templateList = templateName.split('-')
    toJumble = templateList[1:]
    length = len(toJumble)
    combiLength = 2 ** length
    newEntries = []
    entry = []

    for i in xrange(combiLength):
        entry = []
        for j in xrange(length):
            if i >> (length - 1 - j) & 1 == 1:
                entry.append(toJumble[j])
        newEntries.append(' '.join([templateList[0]] + entry))
        newEntries.append('-'.join([templateList[0]] + entry))
    return newEntries
