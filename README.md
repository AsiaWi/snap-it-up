# Snap.it.up

Please note, this README is for backend database of a full stack application. This API provides a backend database to allow all [this](#site-goals) functionality. You can view the [API here](https://snap-it-up-25ef84f951df.herokuapp.com/). To view it in a nicer format install a JSON extension like [this one](https://chromewebstore.google.com/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc) if you're using Chrome.


For details on front-end please visit this link: [FRONT-END REPO](https://github.com/AsiaWi/snap-it-up-frontend/), and if you click [HERE](https://snap-it-up-frontend-0a24e912efd8.herokuapp.com/), you can see live full stack deployed live website.

## Table of Contents

- [Snap.it.up](#Snap-.-it-.-up)
  - [Table of Contents](#table-of-contents)
- [User Experience Design](#user-experience-design)
  - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The Structure Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Database Design](#database-design)
- [Technolgies](#technolgies)
  - [Tools and Technologies](#tools-and-technologies)
  - [Imports](#imports)
    - [Python Packages](#internal-packages)
    - [External Packages](#external-packages)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
    - [Python](#python)
  - [Manual Testing](#manual-testing)
    - [Functional Testing](#functional-testing)
      - [Negative Testing](#negative-testing)
  - [Automatic Testing](#automatic-testing)
    - [Unit Tests](#unit-tests)
- [Bugs](#bugs)
- [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Deploying in Heroku](#deploying-in-heroku)
    - [Cloning the Repository](#cloning-the-repository)
    - [Forking](#forking)
- [Credits](#credits)


# User Experience Design

## The Strategy Plane

### Site Goals

Snap.it.up is an application developed for users to be able to sell their unwanted items. Anyone can register, sign in and create an advert post to sell whatever they no longer need in their life. The website has been designed to be user friendly and make the experience smooth, pleasant and easy. Users can ask questions on the product if unsure of anything, they can conversate on the subject if needed by replying to the question, this way the whole conversation is in one place and users don't have to scroll to find their responses. Once buyers want to purchase an item they can make an offer by submitting a simple form. Seller can then either accept or reject an offer. Seller can accept more than one offer to ensure that item doesn't get stuck unsold if user who's offer has been accepted doesn't contact the seller. This means that whoever acts the fastest and contacts the seller to arrange collection/delivery will get the item. Once the item has been collected and paid for- seller can mark the offer as sold which will change the styling of the advert to show the advert is no longer active and has been sold. This will prevent users from wasting their time on submitting offers as they will know the item is gone. This won't however stop users to interact within the advert- ask questions etc. So if they want to ask if the item will ever be available again etc. they can. The inactive advert styling will also ensure that the seller doesn't have to delete the advert to avoid unwanted contact from users. This will create and show nice history for the seller which will help other users understand how well the seller is doing.
Additionaly users can also search and filter adverts list to easily find what they are looking for, making their experience smooth and enjoyable. Title, tags, location and item description has been included so that users can search by keywords and have bigger possibility of finding something they are looking for (ie. seller included specific key word only within the item description but not in the title). Filtering has been applied to allow users to select a category from drop down box returning a list of items within that category

### Agile Planning

The project was developed using agile methodology. Small features have been assigned to 10 EPICS. This was then divided into 4 sprints.
Labels have been used to mark which features the project : 'must have', 'should have', 'could have'. This was done so that I create a MVP in the time I have and only focus on the 'should have's' or 'could have's' if time allows. 
Each user story was closed if all acceptance criteria have been met.

Project board has been used to help me with the process [PROJECT BOARD-link](https://github.com/users/AsiaWi/projects/5/views/1?layout=board)

![PROJECT BOARD](https://res.cloudinary.com/dmod5eglu/image/upload/v1706064749/project-board_ldpjbh.png)

I have created two additional labels to indicate which user stories required backend work:
  - **API** 
and which ones required front-end work 
  - **React**. 
  
The stories that have both labels will be discussed in each README.
Instead of creating seperate 'developer stories' I created one project workflow that structured my work and allowed me to plan it in less chaotic way.

- API USER STORIES SPRINT1
![API_SPRINT1](https://res.cloudinary.com/dmod5eglu/image/upload/v1706068617/API-SPRINT1_gh6z6u.png)

- API USER STORIES SPRINT2
![API_SPRINT2](https://res.cloudinary.com/dmod5eglu/image/upload/v1706068622/API-SPRINT-2_bqct0v.png)

- API USER STORIES SPRINT3
![API_SPRINT3](https://res.cloudinary.com/dmod5eglu/image/upload/v1706068626/API-SPRINT3_wugxrh.png)

- API USER STORIES SPRINT4
![API_SPRINT4](https://res.cloudinary.com/dmod5eglu/image/upload/v1706068628/API-SPRINT4_ahurxv.png)


#### Epics

- 1-Project setup:
   This was a first task without it I wouldn't be able to continue with any of the project features so it was necessary to set up a basic structure of the project following the user stories included in this Epic.
- 2-Authentication/navigation:
   This milestone was needed to allow users to actually use the page so that the page is interactive
- 3-Advert:
   Includes all features enabling the CRUD functionality for the user
- 4-Adverts page:
   This improves users journey throughout the page and makes it a smooth experience for everyone.
- 5-Questions:
   Includes all features enabling the CRUD functionality for the user
- 6-Replies: 
   Includes all features enabling the CRUD functionality for the user
- 7-Offers:
   Includes all features enabling the CRUD functionality for the user 
- 8-Profile:
   Allows user to CRE own details. Allows other users to find out more about user.
- 9-Rating:
  Includes all features enabling the CRUD functionality for the user
- 10-Documentation and deployment: 
   Absolutely necessary step to make sure the page is deployed with no erros and allows anyone access to all features.Needed to document the project

#### User Stories

 Each EPIC contains user stories allowing me to build up the project with small features:

- EPIC 1- Project setup
  - `As a DEVELOPER I need to SET UP THE PROJECT so that i CAN BUILD THE PAGE`
     - Install Django Rest API
     - Create project
     - Add first main app
     - Add env.py file
     - Add Procfile
     - Install supporting libraries
     - image database - Cloudinary
     - database - ElephantSQL
     - Settings.py edited to notify django of the supporting libraries
     - Project deployed to Heroku
  - `As a DEVELOPER I need to CONNECT THE PROJECT TO CLOUD TO STORE IMAGES so that USERS CAN UPLOAD IMAGES`
- EPIC 2-Authentication/navigation:
  - `As a USER I can REGISTER AND SIGN IN so that I CAN ACCESS CONTENT WHICH REQUIRES TO BE AUTHORISED`
     - install dj-rest-auth add to settings.py
     - install simplejwt library
- EPIC 3-Advert:
  - `As a LOGGED IN USER I can ADD AN ADVERT so that I CAN SHARE IT WITH OTHERS AND SELL ITEMS`
  - `As a USER I can VIEW THE ADVERT POSTS DETAILS so that I LEARN MORE ABOUT IT`
  - `As a LOGGED IN USER I can SAVE AN ADVERT BY CLICKING ON SAVE ICON so that I CAN VIEW IT AGAINST OTHER ITEMS I SAVED/ KEEP AN EYE ON THE ITEM`
  - `As a SELLER I can EDIT MY ADVERTS so that I CAN UPDATE IT OR CORRECT IT IF NEEDED`
  - `As a LOGGED IN USER I can DELETE MY OWNS POSTS so that I CAN KEEP MY ACCOUNT UP TO DATE`
  - `As a USER I can VIEW A POSTED ADVERT so that I CAN FIND OUT ALL DETAILS ABOUT AN ITEM AND SELLER`
  - `As a USER I can SEE ADVERT'S STATUS so that I KNOW IF ITEM IS AVAILABLE OR NOT`
  - `As a USER I can SEE HOW MANY VIEWS EACH POST HAD so that I KNOW HOW POPULAR ARE DIFFERENT ITEMS WITHIN THE PAGE`
  - `As a SELLER OR BUYER I can COMMUNICATE PRIVATELY WITH A BUYER/SELLER ONCE OFFER HAS BEEN ACCEPTED so that I CAN ARRANGE FURTHER DETAILS`
- EPIC 4-Adverts page:
  - `As a USER I can VIEW ALL ADVERTS AS A LIST STARTING WITH MOST RECENT ONES so that I CAN PICK UP ON THE NEWEST DEALS`
  - `As a USER I can SEARCH ADVERTS BY ITEM LOCATION OR KEYWORD/TAG NAME so that I CAN FIND ITEMS THAT I'M INTERESTED IN`
  - `As a USER I can VIEW ITEMS BY CATEGORY so that I CAN FIND ITEMS I NEED`
  - `As a LOGGED IN USER I can SAVE ITEMS so that I CAN GET BACK TO ADVERTS I'M INTERESTED IN EASILY`
  - `As a USER I can VIEW A LIST OF MOST SAVED ITEMS so that I CAN FIND BEST DEALS`
- EPIC 5-Questions:
  - `As a LOGGED IN USER I can ASK A QUESTION ABOUT AN ADVERT so that I CAN GET MORE INFORMATION BEFORE PURCHASE`
  - `As a SELLER I want OTHER USERS TO SEE THE PREVIOUSLY ASKED QUESTIONS AND ANSWERS so that I DON'T HAVE TO ANSWER TO EVERYONE INDIVIDUALLY`
  - `As a SELLER I can SEE A DATE WHEN QUESTION WAS ASKED so that I KNOW IF IT'S STILL RELEVANT OR URGENT`
  - `As a QUESTION OWNER I can EDIT OR DELETE A QUESTION I ASKED so that I CAN CONTROL MY OUTPUT`
- EPIC 6-Replies:
  - `As a LOGGED IN USER I can REPLY TO QUESTIONS so that I CAN COMMUNICATE BACK WITH POTENTIAL BUYERS`
  - `As a BUYER I can VIEW REPLIES LIST TO MY QUESTION BELOW THE QUESTION so that CLARIFY MY CONCERNS`
  - `As a USER I can SEE WHEN SOMEONE REPLIED TO MY QUESTION so that I KNOW IF IT'S MOST RELEVANT`
- EPIC 7-Offers:
  - `As a USER I can SEE ALL PREVIOUSLY MADE OFFERS so that I DON'T WASTE MY TIME MAKING THE SAME OFFERS SELLER ALREADY WASN'T HAPPY WITH`
  - `As a LOGGED IN USER I can MAKE AN OFFER TO A SELLER so that I CAN PURCHASE THE ITEM`
  - `As a SELLER I can ACCEPT OR REJECT AN OFFER RECEIVED so that I CAN SELL AN ITEM AT PRICE I FIND ACCEPTABLE`
  - `As a SELLER I can MARK AN OFFER AS SOLD so that IT'S CLEAR WHICH OFFER WENT THROUGH`
- EPIC 8-Profile:
  - `As a USER I can VIEW EVERYONES PROFILE DETAILS so that I CAN LEARN MORE ABOUT SELLERS/BUYERS:(how long they're active, number of adverts posted, feedback/rating)`
  - `As a PROFILE OWNER I can EDIT MY PROFILE DETAILS so that I CAN KEEP IT UP TO DATE`
  - `As a PROFILE OWNER I can UPDATE PASSWORD AND USERNAME so that I CAN KEEP MY PROFILE SAFE`
- EPIC 9-Rating:
  - `As a LOGGED IN USER I can LEAVE FEEDBACK FOR THE BUYER/SELLER so that OTHERS KNOW HOW RELIABLE THE USER IS`
  - `As a LOGGED IN USER I can RATE A PROFILE ONCE I PURCHASED SOMETHING FROM THE SELLER so that OTHERS KNOW HOW RELIABLE THE SELLER IS`
- EPIC 10-Documentation and deployment:
  - `As a DEVELOPER I need to CREATE README FILE so that I CAN DOCUMENT THE PROCESS OF CREATING THE APPLICATION`
  - `As a DEVELOPER I need to deploy both projects and link them together so that USERS CAN USE FULL STACK WEBSITE`

## The Structure Plane

### Features

#### Homepage

You will see a welcome message, please see the features below where links to all the existing features will be provided

![API-HOME](https://res.cloudinary.com/dmod5eglu/image/upload/v1706113749/API_HOME_rirw05.png)

All features have been implemented with user stories in mind 

#### Advert

- This is a main feature without which the page would not exists, it provides meaning to the app

`As a USER I can VIEW ALL ADVERTS AS A LIST STARTING WITH MOST RECENT ONES so that I CAN PICK UP ON THE NEWEST DEALS`

The advert list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/adverts/

![ADVERTS_VIEW](https://res.cloudinary.com/dmod5eglu/image/upload/v1706069800/API_ADVERTS_VIEW_daw2e8.png)

To see fields included in the model see [Database Design](#database-design) 

Additional fields added with the help of serializer to JSON data:

 - is_owner
 - profile_id
 - profile_image

 `As a USER I can SEE HOW MANY VIEWS EACH POST HAD so that I KNOW HOW POPULAR ARE DIFFERENT ITEMS WITHIN THE PAGE`
 - page_views

 `As a LOGGED IN USER I can SAVE ITEMS so that I CAN GET BACK TO ADVERTS I'M INTERESTED IN EASILY`
 - save_id
 - profile_location
 - save_count

 `As a USER I can SEE ADVERT'S STATUS so that I KNOW IF ITEM IS AVAILABLE OR NOT`
 - active field from model has been set as read only so that the status can get automaticaly change when user sets offer to SOLD.
 - tags have been serialized with TagListSerializerField

Filtering fields have been implemented to:
- Search

`As a USER I can SEARCH ADVERTS BY ITEM LOCATION OR KEYWORD/TAG NAME so that I CAN FIND ITEMS THAT I'M INTERESTED IN`
`As a USER I can VIEW ITEMS BY CATEGORY so that I CAN FIND ITEMS I NEED`
  - By advert_title, tags, item_description, categories, location.
Wide range of search fields has been added that page user has more of a chance of finding something they like with keywords.
- Filter

`As a LOGGED IN USER I can SAVE AN ADVERT BY CLICKING ON SAVE ICON so that I CAN VIEW IT AGAINST OTHER ITEMS I SAVED/ KEEP AN EYE ON THE ITEM`
The saved items list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/saved/
(if user is logged it they can see a form to save an advert. The object will show within a list view. To view the saved item simply follow the URL with the id of the object you can see in the list view)

  - Adverts that have been saved by user to allow users to view a list of adverts they have saved by them as a list 
  - Adverts that have been posted by user so that users can view a list of their own posts only for easy access.
- Order 

 `As a USER I can VIEW A LIST OF MOST SAVED ITEMS so that I CAN FIND BEST DEALS`

  - By save_count, price, created_by, updated_by
To allow ordering of the advert list. 
 
`As a LOGGED IN USER I can ADD AN ADVERT so that I CAN SHARE IT WITH OTHERS AND SELL ITEMS`

`As a USER I can VIEW THE ADVERT POSTS DETAILS so that I LEARN MORE ABOUT IT`

`As a SELLER I can EDIT MY ADVERTS so that I CAN UPDATE IT OR CORRECT IT IF NEEDED`

`As a LOGGED IN USER I can DELETE MY OWNS POSTS so that I CAN KEEP MY ACCOUNT UP TO DATE`

Once user is logged in, form to submit an advert becomes available. Once submitted, user will see their ad as an additional object to the list view. If user uses the id from the object and follows current URL with `/id` they can access advert detail view where if authorised (ie. adverts 'is_owner' field =true) they will be able to edit/delete the advert.




## The Skeleton Plane

### Database design

![entity_relationship_diagram](https://res.cloudinary.com/dmod5eglu/image/upload/v1706121326/ER_DIAGRAM_bazv82.png)

- The ER Diagram has been generated with DBeaver. 
- The diagram shows relationships between models
  - The user model supports pretty much all existing features and allows user to interact with posts when logged in with the help of foreign key
  - Advert related to user model allowing users to perform CRUD funcionality
  - Questions relate to advert model and user model allowing users to send queries in regards to specific add.
  - Replies relate to questions and user model, allowing users to answer to specific question and keep track of conversation
  - Rating model relates to User and checks logged in user (owner of rating) and rated user with the help of foreign key
  - Offers relate to user model and advert, with the help of foreign key offers can be placed on specific advert, buyer_id helps to allocate offer to owner and seller_id allows seller to change offer status
  - Save model related to advert and user to allow users to save favourite ads.
  - Profile related to User model
  - Hitcount model has been implemented to count page views for each advert, hit count relates to User model saving User ID each active session
  - Taggit related to content type and taggit_tag allowing me to implement function to add tags for users
