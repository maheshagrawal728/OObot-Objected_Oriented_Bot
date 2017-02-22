### Team OObot:

- ajagana - Arun Jaganathan
- mramali2 - Mathioli Ramalingam
- rchandh - Ravishankar Chandhiramoorthi
- pkattep - Pranesha Shashwath Kumar Kattepura Jayabheema Rao
- mlakshm - Muthu Arvind Lakshmanan

### Changes suggested by the professor :

- Fix problem statement
- Bot interaction to be made more brief and concise
- Fix wireframes and storyboard
- Pick better patterns

The above changes were incorporated and following is the new Design.

##Problem statement:

When you want to create a new application and know which design pattern to use but not sure how to start OObot comes to your rescue. OObot provides starter code for the design pattern you have chosen. If the bot does not have starter code for the the design pattern you specified it is ready to learn from you. Also, the bot can use GitHub apis to search for starter code for any design pattern in GitHub for you.

##Bot Description
The bot, when asked for an architectural design pattern, will retrieve the template code for that pattern from its database and provide a github link to the generated code. 
The user is expected to provide the name of the pattern they are looking for and the bot will parse this information and retrieve the appropriate entry from the database.
If the pattern provided by the user is available, the Bot would create a branch in the user’s Git Repository and push the code. 
In case the pattern provided by the user is not available in the database, then the bot can do the following - 
 - The user can provide his own implementation of the pattern and the bot will store this in its database and 
 retrieve it when asked in the future. 
 - The bot can search for the pattern using the github API and provide a link to an existing repository if it is present.

###Storyboard:

![Alt text](/imgs/Storyboard1.JPG 'Storyboard')
![Alt text](/imgs/Storyboard2.JPG 'Storyboard')
![Alt text](/imgs/storyboard3.JPG 'Storyboard')
![Alt text](/imgs/storyboard4.JPG 'Storyboard')
![Alt text](/imgs/storyboard5.JPG 'Storyboard')

##Design Sketches

![Alt text](/imgs/wireframe1.png 'Wireframe')
![Alt text](/imgs/wireframe2.png 'Wireframe')

##Architecture Design

The architecture will have three major components:
- A slack bot for interacting with the user.
- A server which can be used to process the message from user and take appropriate actions
- A datastore to store the design patterns.

In addition, the server will also use GitHub APIs to search the GitHub for certain patterns.

![Alt text](/imgs/Architecture Diagram.png 'Architecture Diagram')

##Use cases

The following are the use cases that we are planning to cover up
- User Requests for a template code for a design pattern via Slackbot. 
- The user wants to provide his template code for a particular pattern, to be saved in the data store.
- Search for a design pattern in GitHub, if design pattern unavailable in the data store.

### Programming Languages:

- Python
- Java

### The patterns for which bot will generate code

- Publish-subscribe pattern
- IoT command and control pattern
- Space Reactor bot
- Conversation bot pattern

##Constraints

The following are the constraints of the bot
- It is assumed that the user knows what pattern they are looking for.
- The bot cannot edit code or improve upon an existing design pattern based on the user’s needs.
- The user has to specify the name of the repository and also add the Bot as a collaborator in his/her Github Repository. 
- The bot has its own implementations for a limited number of freestyle patterns.

For future work, the bot should ideally be able to identify the appropriate pattern for a use case provided by the user. 
For example,if the user says he is working on a parser,
then the bot should provide a github link to the template code of the interpreter pattern.

