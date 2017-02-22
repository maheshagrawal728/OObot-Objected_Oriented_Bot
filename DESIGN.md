# OObot

## Problem statement:

When we try to create a new application, its very hard to completely comprehend which objects are involved, relationships involved between them and which design pattern should be applied to make the code less complex, cohesive and loosely coupled. Its very easy to start with an inefficient code and make it non-scalable. We sense a strong need for starter code for any project which gives developers the right direction to think and keep the code loosely coupled and more scalable.

##Bot description:

The bot we are proposing generates a object oriented starter code given minimum details about the problem statements. Once we get minimum data, bot will generate a basic code and display it to the user. User can add an additional requirement. Then we ask questions which will make the understanding of new requirement concrete and quantifiable. Based on this understanding we use an appropriate design pattern to update the code.

We will need details such as follows to create a basic starter code:
- Who are the end-users?
- Who is the service provider (or) the people or object users are trying to connect to?
- Is it one-to-one or many-to-one relationship between client and service providers?
- Constraints and how the problem is expected to scale?

Once done, user can ask for an additional requirement. It could be something like:
- I want different types of users
- Want to create a new class
- Want another class with only one instance

In next wire frame we would ask more questions to make the requirement more concrete; then apply a design pattern to update the code. We will repeat the process of adding a new requirement and updating the code repeatedly till user is done with the code or its too complex to handle further.


## Design sketches:
![Alt text](/imgs/Requirements_Page_1.png 'requirements')
![Alt text](/imgs/Code_Preview_Page_2.png 'code preview')
![Alt text](/imgs/Questions_Page_3.png 'questions')
![Alt text](/imgs/Thank_You_Page_4.png 'thank_you')
    

##Architecture Design:

The architecture will have four major components:
- The bot UI will take inputs from the user
- Then the based on the question logic we create code relevant to the given requirements
- Now, user might ask additional requirement
- Based on the existing code and the requirement asked we ask specific questions required to make further design decision of the code. - For this we might fetch some rules from the data store as well.
- Based on user’s answers we make changes to design of the existing code and show the updated code to the user.
- Repeat steps from 3 to 5 till user is done (or) it is too compl

![Alt text](/imgs/archDiagram.jpg 'arch deiagram')


###Use cases:

2 or 3 of the following -
Social network (ex: facebook), factory (ex: Form motors), crowd-sourced review system (ex: Yelp), institute (ex: library)

###Design Patterns the bot will handle:

- Observer
- Factory
- Facade
- Strategy
- Iterator

###Constraints:

We would be able to handle only selected use cases.

The creation of the code has to be generated in one sitting. User cannot save the code and come back for more. This might affect the internal decision trees regarding design pattern selection, etc.

##Additional Patterns:

In our current understanding of the project we will be using following patterns in our project:

- Factory - to be able to generate code of different types based on a decision tree input rather than creating a separate class for each use case
- Facade - different backend logics are handled through same user interface
- Observer - handling events created from user and make the code generation more and more refined

