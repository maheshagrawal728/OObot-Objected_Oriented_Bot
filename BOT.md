## Use cases:

###Use case 1: 
User Request for template code for a design pattern

- Preconditions

The client code should have the credentials and api’s to fetch the template from the data store when requested by the user. It should have github api’s to create new branch and upload files. If the user wants the bot to upload the files to user’s repo, the bot should be added as collaborator to the user’s repo.

- Main Flow

User will request a design pattern template

- Subflows

	[S1] Bot provides options on whether the user wishes to download the template locally or upload to a github repo
	[S2] User provides with github credentials like repo name. Bot will create a branch in the given repo and post the link to the repo with the uploaded template.
	
- Alternative Flows
[E1] User requested design pattern is not available

###Use case 2: 

The user wants to provide his template code for a particular pattern
- Preconditions

The bot should not have the provided pattern


- Mainflow

	The user says he wants to provide a new pattern. The bot then gets the github repository of the user’s code and stores it internally for future use.
- Subflows

	[S1] The bot can clone the repository and have its own version of the code.
- Alternative Flows

	[E1] The design pattern provided by the user is already present and the bot notifies about this to the user.

###Use case 3: 

Search for a design pattern in GitHub

- Preconditions
  
	Require GitHub apis to search in GitHub

- Main Flow
  
	The user will request to fetch a design pattern from GitHub
- Subflows
  
	[S1] User provides design pattern which needs to be fetched from GitHub
  	[S2] Bot searches through GitHub and provides repo link if it finds a repo for the design pattern. 

- Alternative Flow

  	[E1] No repo available for given design pattern

## Mocking:

For this milestone, we are using a mock data to successfully showcase the BOT implmentation. All the GitHub links that the BOT throws are dummy links. The mock.json contains links for different patterns, and also mock search results which are leveraged for the Bot implementation

## Bot Implementation:

Refer [here](https://github.ncsu.edu/pkattep/OObot/tree/master/code) for Bot Implementation.

- startbot.py
- chatbot.py 
- mockit.py 
- mock.json  

## Selenium Testing:

Refer [here](https://github.ncsu.edu/pkattep/OObot/tree/master/Selenium) for files related to selenium testing.

Importantly, refer to this file,
[WebTest.java](https://github.ncsu.edu/pkattep/OObot/blob/master/Selenium/src/test/java/selenium/tests/WebTest.java)

## Task Tracking :

[Worksheet](https://github.ncsu.edu/pkattep/OObot/blob/master/WORKSHEET.md)

## Extra credits : 

Refer [here](https://github.ncsu.edu/pkattep/OObot/tree/master/Sauce) for files ( Screenshots and logs) related to sauce testing.

For Travis ci, the logs files can be viewed in the travis folder.

## Screencast:

[OObot Funcitonality](https://youtu.be/0QaKxRMLv68)

[Selenium Testing](https://youtu.be/sjk_CKh4lxI)

[Sauce Testing](https://youtu.be/lFrt5dDyyNk)

