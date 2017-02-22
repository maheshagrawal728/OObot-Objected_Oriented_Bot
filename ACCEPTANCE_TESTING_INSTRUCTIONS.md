# Acceptance Test Instructions:

For all the interactions with the bot, the user should start the conversation with @oobot, followed by the message
## Use case 1: User Request for template code for a design pattern

###  Preconditions

The client code should have the credentials and api’s to fetch the template from the data store when requested by the user. It should have github api’s to create new branch and upload files. If the user wants the bot to upload the files to user’s repo, the bot should be added as collaborator to the user’s repo.The link the user provides should be a NCSU enterprise github link, i.e., it should be from github.ncsu.edu and not form github.com


### 2. Main Flow

User will request a design pattern template:

**Possible requests** -
- Can you fetch publish-subscribe pattern
- Can you give me publish-subscribe pattern
- Can you get iot command control template
- Can you get me pubsub pattern
- need factory pattern
- need factory template
- want factory pattern
- get/need factory pattern/template?

The bot will look-up for the words like give, provide, get, fetch and parses the word ‘xxxxx pattern’ and requests for the language of the code. 

####    Constraint: The user should not request like 'I need factory pattern" or 'I want factory pattern'. Rather, user requests should be as mentioned above. If given 'I', the flow gets redirected to usecase2.
  

### 3. Subflows

[S1] Bot provides options on whether the user wishes to download the template locally or upload to a github repo
If bot understands your request to be use case 1 then it will ask you if you would like to download the code or upload it in one of your repos

[S2] User provides with github credentials like repo name. Bot will create a branch in the given repo and post the link to the repo with the uploaded template.

**Upload**: If you provide a string with the word ‘upload’ or ‘clone’ in it, then the bot will ask for github username and repo name and add ‘rchand’ as collaborator. (It is with his GitHub token that we are launching our GitHub apis)
Then the bot will upload the pattern in the user’s repo in a new branch ‘oobot’

**Download**: Or else if you provide a string with ‘download’ in it, then the bot will provide a link to download the code for the pattern. When you click on the link it will download the pattern.

### 4. Alternative Flows

[E1] User requested design pattern is not available
If the pattern requested by the user is not present in the organization maintained for the bot then the bot apologizes saying the pattern is not present in the organization. Then the use-case ends.


## Use case 2: The user wants to provide his template code for a particular pattern

### Preconditions

- The bot should not have the provided pattern in that language.
- The link that user provides should be from github.com only, and not from github.ncsu.edu or other enterprise accounts

### 2. Mainflow

The user says he wants to provide a new pattern along with the language. The bot then gets the github repository of the user’s code and stores it internally for future use.

**Possible requests** -
- Can you store a pattern?
- Can you save a template
- Can you keep a template
- Can I give you pubsub pattern
- I am giving/providing factory pattern. store it
- can i give/provide/put factory pattern?

**Learn a pattern**
The bot then requests the user to provide the URL along with the language and replies that the pattern has been added successfully, if everything goes as expected.

### 3. Subflows

[S1] The bot can clone the repository and have its own version of the code.
The bot will ask for pattern name,language in which the pattern name is present and repo link
Then the bot will upload the repository in organization of the bot with repo name same as the pattern name provided by the user.

### 4. Alternative Flows

[E1] The design pattern provided by the user is already present and the bot notifies about this to the user.
If we provide a pattern that already exists then the bot will mention that the pattern already exists and ends the use-case


## Use case 3: Search for a design pattern in GitHub

### 1 Preconditions

- Require GitHub apis to search in GitHub
- Searches and retrieves results from github.com only

### 2 Main Flow

The user will request to fetch a design pattern from GitHub

**Possible requests** -
- Can you search for a pattern from github
- Can you search template from github
- search for a pattern in github
- lookup for factory pattern
- need/want/search factory pattern from github

### 3 Subflows

[S1] User provides design pattern which needs to be fetched from GitHub
After the above request the bot will ask to provide the pattern, programming language
The user is expected to provide a pattern name, desired programming language

[S2] Bot searches through GitHub and provides repo link if it finds a repo for the design pattern.
The bot searches through the GitHub and provides most relevant links of repos for the given pattern name, programming language 

### 4 Alternative Flow

[E1] No repo available for given design pattern
If no repo could be found for the given pattern for the given programming language then an error message is thrown

