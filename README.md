# OObot---Objected-Oriented-Bot
A Python bot (Slackbot) that provides starter template code for a design pattern, either from the Bot’s repository or from GitHub’s store, based on User’s request– implemented using GitHub APIs

## ScreenCast 

#### [A 3 minute summary of the Bot](https://www.youtube.com/watch?v=KKupHeuscwo)
#### [Demo of the Bot](https://www.youtube.com/watch?v=o9J6Zlc6VDw)

## Problem statement:

When you want to create a new application and know which design pattern to use but not sure how to start OObot comes to your rescue. OObot provides starter code for the design pattern you have chosen. If the bot does not have starter code for the the design pattern you specified it is ready to learn from you. Also, the bot can use GitHub apis to search for starter code for any design pattern in GitHub for you.

## Bot Description
The bot, when asked for an architectural design pattern, will retrieve the template code for that pattern from its database and provide a github link to the generated code. 
The user is expected to provide the name of the pattern they are looking for and the bot will parse this information and retrieve the appropriate entry from the database.
If the pattern provided by the user is available, the Bot would create a branch in the user’s Git Repository and push the code. 
In case the pattern provided by the user is not available in the database, then the bot can do the following - 
 - The user can provide his own implementation of the pattern and the bot will store this in its database and 
 retrieve it when asked in the future. 
 - The bot can search for the pattern using the github API and provide a link to an existing repository if it is present.

## Architecture Design

The architecture will have three major components:
- A slack bot for interacting with the user.
- A server which can be used to process the message from user and take appropriate actions
- A datastore to store the design patterns.

In addition, the server will also use GitHub APIs to search the GitHub for certain patterns.

![Alt text](/imgs/Architecture Diagram.png 'Architecture Diagram')

### Programming Languages:

- Python
- Java

### The patterns for which bot will generate code

- Publish-subscribe pattern
- IoT command and control pattern
- Space Reactor bot
- Conversation bot pattern


## The problem the bot solved

With most development teams following the agile process, programmers are constantly looking to develop products in ways that are fast and efficient. However, developers have often been forced to choose one of two by either compromising quality for speed or vice versa. One way to avoid such a trade off and stay ahead in the process, is to start the development phase by identifying a suitable design pattern for the use case and start the coding step with an established template code. These patterns need not necessarily be part of the mainstream design patterns that we usually see in object oriented programming, but could be custom templates developed by programmers to solve generalizable use cases. Our bot provides programmers with such templates and also lets them share their implementations with other programmers or teams. By making starter code readily available, we believe our bot will help boost productivity of developers and also help them follow standards thereby letting them build clean, efficient and maintainable software products.   

## Use cases

The following are the use cases that we are planning to cover up
- User Requests for a template code for a design pattern via Slackbot. 
- The user wants to provide his template code for a particular pattern, to be saved in the data store.
- Search for a design pattern in GitHub, if design pattern unavailable in the data store.

The OOBOT has a data store where it can store all the pattern template. The data store we used for the bot is GitHub repo. We have created an organization ‘OOBOT’ in GitHub, which will act as a data store for the bot. The bot currently supports programming language Java and Python, but the developer community has an option to upload the pattern template for other languages as well.

We have addressed three important scenarios using our bot. When a developer needs a template for particular pattern, he/she can ask the bot for the template, if the bot does not have a template, the user can search the GitHub for the template using our bot, and user can upload the template they have, to help other developers in the community.

#### Ask the bot for a template

The developer can ask the bot for a pattern template and they also have an option to specify their preferred language. The bot searches for the template in its pattern template pool and provides the user the requested template. The bot can provide the template in two different ways, either provide the download url or option to upload the template into the developer’s repo directly. If the developer opt for the upload option, he/she has to add the bot as the collaborator.

![Alt text](Report/usecase1_flow1.png?raw=true "")
![Alt text](Report/usecase1_flow2.png?raw=true "")

#### Upload template to the bot

The main idea for this bot is to help the developer community with the starter code. We should not confine with the template we have, so we have provided an option for the community to share their code with others. If the developer has a template for a pattern which the bot does not have, they can upload their pattern to the bot’s pattern template pool. The bot cannot validate the code that is being uploaded. The developer has to be responsible for uploading valid code to the pool.

![Alt text](Report/usecase2.png?raw=true "")

#### Ask the bot to search for a template

If the developer was not able to find the desired template in the bot’s pattern template pool, he/she can still find the template, by using the search feature in our bot. Our bot will search the GitHub’s repo for the template, and provide the list of url’s to the user.

![Alt text](Report/usecase3.png?raw=true "")

## Reflection on the development process and project

#### Agile
Throughout the project we followed agile manifesto of giving more importance to working software over documentation, and collaborated more than negotiating with each other. We discussed different approaches of where and how to implement a particular feature. For example: while discussing which repository we need to for different different pattern codes we considered firebase, AWS or git itself. After considering pros and cons on cost, efficiency and flexibility we decided to work with git. For the first few meetings all of us were compulsorily present in order to ideate and come up with the best approaches. As and when we found issues in development we did pair programming in order to figure where the problems were. 4 eyes were always more sensitive to bugs than 2 eyes. We also had a slack team to discuss the progress and updates regarding the project development.

#### Documenting Responsibilities through issues
For the first time we documented and all the different responsibilities in git issues. This gave us a sense of responsibility and importance as we worked through our different responsibilities. It was also easy for the team to track that a related task was already assigned to a teammate. This was reassuring since we have been in position when we did not know who was doing a related task, panicked and msged in our whatsapp groups who was doing what. Git also did an amazing job by notifying us through email when a new task was created or closed.

#### Integration was much easier with shared responsibilities
As the tasks were divided and documented in github issues we knew exactly whom to contact while working on a particular component than flooding the message in our chat group. We could discuss collaborate and come up with a common way to integrate the 2 related components together.

Another major advantage was that not everyone had to meet together for bugs related to a particular feature. Only those working on the related components would have a private meeting and complete the task. This saved the time of team as a whole.

#### Assigned responsibilities for resolving issues
Also, as and when we found some unexpected bugs along the development task we documented them in git issues and assigned responsibility to two of the team members. This encouraged pair programming for resolving issues quickly and effectively. The team synchronization was so well developed towards the end of the project that we did not have to meet very often for the last milestone. Everyone knew exactly what the other person was working on and how to go about his task.


## Constraints:
The following are the constraints of the bot
- It is assumed that the user knows what pattern they are looking for.
- The bot cannot edit code or improve upon an existing design pattern based on the user’s needs.
- The user has to specify the name of the repository and also add the Bot as a collaborator in his/her Github Repository. 
- The bot has its own implementations for a limited number of freestyle patterns.


## Future work:

#### Code validation:
Right now our bot is not validating the code the user gives in usecase 2. We could add a provision for another user to validate it or crowd source the feedback from users who received the code from usecase 1.


#### Improved conversation:
We could use NLTK library to have a better and more robust conversation with the bot and have more variety of responses. This would give a better user experience.


#### Integrating usecase 1 and usecase 3:
We could integrate usecase 1 and usecase 3 to search a pattern from GitHub in case we could not find that pattern in our pool or repos.


#### Understanding the design pattern the user wants by having a conversation with the user:
Sometimes a user might not know which pattern he wants. In that case we might have to have a conversation with the user and have a predictive model to predict what pattern the user actually wants and provide him that pattern




