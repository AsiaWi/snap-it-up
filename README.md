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
- [Technologies](#technologies)
  - [Tools and Technologies](#tools-and-technologies)
  - [Imports](#imports)
    - [Installed Packages](#installed-packages)
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

and which ones required front-end work:

  - **React**. 
  
The stories that have both labels will be discussed in each README.
Instead of creating seperate 'developer stories' I created one project workflow that structured my work and allowed me to plan it in less chaotic way.

- API USER STORIES SPRINT1
![API_SPRINT1](https://res.cloudinary.com/dmod5eglu/image/upload/v1706068617/API-SPRINT1_gh6z6u.png)

- API USER STORIES SPRINT2
![API_SPRINT2](https://res.cloudinary.com/dmod5eglu/image/upload/v1706068622/API-SPRINT-2_bqct0v.png)

- API USER STORIES SPRINT3
![API_SPRINT3](https://res.cloudinary.com/dmod5eglu/image/upload/v1706068626/API-SPRINT3_wugxrh.png)
![API_SPRINT3_PART2](https://res.cloudinary.com/dmod5eglu/image/upload/v1706194186/API_SPRINT3_PART2_l7zsb4.png)
- API USER STORIES SPRINT4
![API_SPRINT4](https://res.cloudinary.com/dmod5eglu/image/upload/v1706068628/API-SPRINT4_ahurxv.png)
![API_SPRINT4_PART2](https://res.cloudinary.com/dmod5eglu/image/upload/v1706137454/API_SPRINT4_2_dhotwi.png)

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
  - `As a DEVELOPER I need to CONNECT THE PROJECT TO CLOUD TO STORE IMAGES so that USERS CAN UPLOAD IMAGES`
- EPIC 2-Authentication/navigation:
  - `As a USER I can REGISTER AND SIGN IN so that I CAN ACCESS CONTENT WHICH REQUIRES TO BE AUTHORISED`
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
  - `As a LOGGED IN USER I can EDIT/DELETE MY REPLY so that MANAGE MY INPUT`
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
  - `As a USER I can EDIT OR DELETE RATING I HAVE LEFT so that I CONTROL MY INPUT`
  - `As a SELLER AND BUYER I can SEE WHEN RATINGS HAVE BEEN LEFT FOR USERS so that I KNOW IF IT'S SAFE TO USE THEM`
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

`As a LOGGED IN USER I can ADD AN ADVERT so that I CAN SHARE IT WITH OTHERS AND SELL ITEMS`

The advert list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/adverts/

    -Endpoint ``/adverts/``
    -Methods used:
     `GET`  used to list view adverts
     `POST` used to create an advert

![ADVERTS_VIEW](https://res.cloudinary.com/dmod5eglu/image/upload/v1706069800/API_ADVERTS_VIEW_daw2e8.png)

To see fields included in the model see [Database Design](#database-design) 

Additional fields added with the help of serializer to JSON data:

 - is_owner
 - profile_id
 - profile_image

 `As a USER I can SEE HOW MANY VIEWS EACH POST HAD so that I KNOW HOW POPULAR ARE DIFFERENT ITEMS WITHIN THE PAGE`
 
 - page_views
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
  - Adverts that have been saved by user to allow users to view a list of adverts they have saved by them as a list 
  - Adverts that have been posted by user so that users can view a list of their own posts only for easy access.
- Order 

 `As a USER I can VIEW A LIST OF MOST SAVED ITEMS so that I CAN FIND BEST DEALS`

  - By save_count, price, created_by, updated_by
To allow ordering of the advert list. 

`As a USER I can VIEW THE ADVERT POSTS DETAILS so that I LEARN MORE ABOUT IT`

`As a SELLER I can EDIT MY ADVERTS so that I CAN UPDATE IT OR CORRECT IT IF NEEDED`

`As a LOGGED IN USER I can DELETE MY OWNS POSTS so that I CAN KEEP MY ACCOUNT UP TO DATE`

    -Endpoint `/adverts/int:pk/`
    -Methods:
     `GET`  used to get an advert
     `PUT`  used to edit an advert
     `DELETE` used to delete an advert

Once user is logged in, form to submit an advert becomes available. Once submitted, user will see their ad as an additional object to the list view. If user uses the id from the object and follows current URL with `/id` they can access advert detail view where if authorised (ie. adverts 'is_owner' field =true) they will be able to edit/delete the advert.

#### Save

 `As a LOGGED IN USER I can SAVE AN ADVERT BY CLICKING ON SAVE ICON so that I CAN VIEW IT AGAINST OTHER ITEMS I SAVED/ KEEP AN EYE ON THE ITEM`
 ``As a LOGGED IN USER I can SAVE ITEMS so that I CAN GET BACK TO ADVERTS I'M INTERESTED IN EASILY`
 (acceptance criteria:save item when logged in)


The saved items list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/saved/

      -Endpoint `/saved/int:pk/`
      -Methods:
      `GET`  used to list view saved adverts
      `POST` used to save an advert

![SAVED_ITEMS_VIEW](https://res.cloudinary.com/dmod5eglu/image/upload/v1706126806/API_SAVED_ITEMS_VIEW_xnqews.png)

To see fields included in the model see [Database Design](#database-design) 

Serializer:

 - owner field from model set to read only so that user can click on the item as it get's their username

The unique together Meta class ensures that user can save specific item only once and doesn't store duplicates in their saved items list
 
``As a LOGGED IN USER I can SAVE ITEMS so that I CAN GET BACK TO ADVERTS I'M INTERESTED IN EASILY`
 (acceptance criteria:remove saved item when logged in)

      -Endpoint `/saved/int:pk/`
      -Methods:
       `DELETE` used to remove save from advert

Once user is logged in, form to save advert becomes available. Once submitted, user will see their ad as an additional object to the list view. If user uses the id from the object and follows current URL with `/id` they can access saved object detail view where if authorised (ie. adverts 'owner' field =true) they will be able to edit/delete the save.

#### Questions

`As a SELLER I want OTHER USERS TO SEE THE PREVIOUSLY ASKED QUESTIONS AND ANSWERS so that I DON'T HAVE TO ANSWER TO EVERYONE INDIVIDUALLY`

 `As a LOGGED IN USER I can ASK A QUESTION ABOUT AN ADVERT so that I CAN GET MORE INFORMATION BEFORE PURCHASE`

The questions list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/questions/


      -Endpoint `/questions/`
       `GET`  used to list view questions
       `POST` used to create a question

![API_QUESTIONS_VIEW](https://res.cloudinary.com/dmod5eglu/image/upload/v1706128036/api_questions_view_dcinee.png)

To see fields included in the model see [Database Design](#database-design) 

Additional fields added with the help of serializer to JSON data:

 - is_owner
 - asked_by_profile_user
 - profile_image
 - replies_count
 - replies
 Replies field has been added as I think it makes the experience much easier to see full conversation in one place.

`As a SELLER I can SEE A DATE WHEN QUESTION WAS ASKED so that I KNOW IF IT'S STILL RELEVANT OR URGENT`

`naturaltime` has been implemented to updated_at and created_at for more human friendly timestap. This allows users to easily see when message has been posted.

Filtering fields have been implemented to:
- Filter backend
  - By advert so that questions can be displayed under correct advert on front end.
Questions have been ordered in descending order so that the newest questions are at the top and others easily see if anything needs attention
 
 `As a QUESTION OWNER I can EDIT OR DELETE A QUESTION I ASKED so that I CAN CONTROL MY OUTPUT`
  
        -Endpoint `/questions/int:pk/`
        -Methods:
          `GET`  used to list view questions
          `PUT`  used to edit question
          `DELETE` used to delete a question

Once user is logged in, form to submit a question becomes available. Once submitted, user will see their question as an additional object to the list view. If user uses the id from the object and follows current URL with `/id` they can access question detail view where if authorised (ie. questions 'is_owner' field =true) they will be able to edit/delete the object. The advert field has been set to read only in detail view to avoid repetition when editing.

#### Replies

 `As a BUYER I can VIEW REPLIES LIST TO MY QUESTION BELOW THE QUESTION so that CLARIFY MY CONCERNS`

  `As a LOGGED IN USER I can REPLY TO QUESTIONS so that I CAN COMMUNICATE BACK WITH POTENTIAL BUYERS`

The replies list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/replies/

       -Endpoint `/replies/`
       -Methods:
         `GET`  used to list view replies
        `POST`  used to create a reply
    
![API_REPLIES_VIEW](https://res.cloudinary.com/dmod5eglu/image/upload/v1706129129/API_REPLIES_VIEW_t25qqe.png)

To see fields included in the model see [Database Design](#database-design) 

Additional fields added with the help of serializer to JSON data:

 - is_owner
 - created_by_profile_user
 - profile_image

`As a USER I can SEE WHEN SOMEONE REPLIED TO MY QUESTION so that I KNOW IF IT'S MOST RELEVANT`

`naturaltime` has been implemented to updated_at and created_at for more human friendly timestap. This allows users to easily see when message has been posted.

Filtering has been implemented to:
- Filter backend
  - By question so that replies can be displayed under correct question on front end.
Replies have been ordered in descending order so that the newest questions are at the top and others easily see if anything needs attention
 
 `As a LOGGED IN USER I can EDIT/DELETE MY REPLY so that MANAGE MY INPUT`

       -Endpoint `/replies/int:pk/`
        -Methods:
        `GET`  used to list view replies
        `PUT`  used to edit a reply
        `DELETE` used to delete a reply

Once user is logged in, form to submit the reply becomes available. Once submitted, user will see their reply as an additional object to the list view. If user uses the id from the object and follows current URL with `/id` they can access reply detail view where if authorised (ie. reply 'is_owner' field =true) they will be able to edit/delete the object. The question field has been set to read only in detail view to avoid repetition when editing.

#### Offers

 `As a USER I can SEE ALL PREVIOUSLY MADE OFFERS so that I DON'T WASTE MY TIME MAKING THE SAME OFFERS SELLER ALREADY WASN'T HAPPY WITH`

 `As a LOGGED IN USER I can MAKE AN OFFER TO A SELLER so that I CAN PURCHASE THE ITEM`

The offers list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/offers/

       -Endpoint `/offers/`
       -Methods:
        `GET`  used to list view offers
        `POST`  used to create an offer

![API_OFFERS_VIEW](https://res.cloudinary.com/dmod5eglu/image/upload/v1706129810/API_OFFERS_VIEW_hl97ex.png)

To see fields included in the model see [Database Design](#database-design) 

PLEASE NOTE `MESSAGE` FIELD HAS BEEN DELETED FROM OFFER MODEL SINCE THE DATABASE DIAGRAM HAS BEEN ADDED TO README

Additional fields added with the help of serializer to JSON data:

 - created_by_profile_user
 - profile_image

`naturaltime` has been implemented to updated_at and created_at for more human friendly timestap. This allows users to easily see when message has been posted.

Filtering has been implemented to:
- Filter backend
  - By advert so that offers can be displayed under correct advert on front end.
Offers have been ordered in descending order so that the newest offers are at the top as most up to date.

`As a SELLER I can ACCEPT OR REJECT AN OFFER RECEIVED so that I CAN SELL AN ITEM AT PRICE I FIND ACCEPTABLE`

``As a SELLER I can MARK AN OFFER AS SOLD so that IT'S CLEAR WHICH OFFER WENT THROUGH``

          -Endpoint `/offers/int:pk/`
          -Methods:
           `GET`  used to view offers
           `PUT` used to edit an offer (status)
          
Once user is logged in, form to submit the offer becomes available. Once submitted, user will see their offer as an additional object to the list view, status field is set to pending as default. If user uses the id from the object and follows current URL with `/id` they will not have an edit option unless they are a 'seller'. This is because only seller will have an access to  change status of the offer to either accepted or rejected and then again if purchase goes through they can go back and change status to sold which will also set related adverts 'active field' to false( This is mostly with intention of setting styling on front end to show the item has been sold without seller having to delete the item). Fuctionality to delete has not been implemented intentionaly so that other potential buyers don't make the same offers and can see what seller isn't already happy to accept.

#### Profile

The profiles list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/profiles/
 
          -Endpoint `/profiles/`
          -Methods:
          `GET`  used to list view profiles

![API_PROFILES_VIEW](https://res.cloudinary.com/dmod5eglu/image/upload/v1706135071/API_PROFILE_VIEW_xz5lrt.png)

To see fields included in the model see [Database Design](#database-design) 

Additional fields added with the help of serializer to JSON data:

 - is_owner
 - advert_count
 - rating_count
 - average_rating

`naturaltime` has been implemented to created_at for more human friendly timestap. This allows users to easily see when message has been posted.

Filtering has been implemented to:
- Filter backend
  - By '-average_rating" this has been done for front end purposes, to display highest rated profiles in side bar desktop view only.

  `As a USER I can VIEW EVERYONES PROFILE DETAILS so that I CAN LEARN MORE ABOUT SELLERS/BUYERS:(how long they're active, number of adverts posted, feedback/rating)`

  `As a PROFILE OWNER I can EDIT MY PROFILE DETAILS so that I CAN KEEP IT UP TO DATE`

  `As a PROFILE OWNER I can UPDATE PASSWORD AND USERNAME so that I CAN KEEP MY PROFILE SAFE`

            -Endpoint `/profiles/int:pk/`
            -Methods:
            `GET`  used to view profile
            `PUT`  used to edit profile

No option to create profile from list view as this is automatically done upon registration with a help of signal created. If user uses the id from the profile object and follows current URL with `/id` they can access profile detail view where if authorised (ie. profiles 'is_owner' field =true) they will be able to edit the profile.

#### Rating

   `As a LOGGED IN USER I can LEAVE FEEDBACK FOR THE BUYER/SELLER so that OTHERS KNOW HOW RELIABLE THE USER IS`
   `As a LOGGED IN USER I can RATE A PROFILE ONCE I PURCHASED SOMETHING FROM THE SELLER so that OTHERS KNOW HOW RELIABLE THE SELLER IS`

The rating list view can be accessed here: https://snap-it-up-25ef84f951df.herokuapp.com/ratings/

        -Endpoint `/ratings/`
        -Methods:
        `GET`  used to list view ratings
        `POST`  used to create a rating

![API_RATINGS_VIEW](https://res.cloudinary.com/dmod5eglu/image/upload/v1706137759/API_RATING_VIEW_vgsfz8.png)

To see fields included in the model see [Database Design](#database-design) 

Additional fields added with the help of serializer to JSON data:

 - is_owner
 - profile_image

`As a SELLER AND BUYER I can SEE WHEN RATINGS HAVE BEEN LEFT FOR USERS so that I KNOW IF IT'S SAFE TO USE THEM`

`naturaltime` has been implemented to updated_at and created_at for more human friendly timestap. This allows users to easily see when message has been posted.

Filtering fields have been implemented to:
- Filter backend
  - By 'rated_user' so that ratings can be displayed against correct rated profile on front end.
Ratings have been ordered in descending order so that the newest questions are at the top so users can hear about most recent experiences with the profile user.
 
 `As a USER I can EDIT OR DELETE RATING I HAVE LEFT so that I CONTROL MY INPUT`
         
         -Endpoint `/ratings/int:pk/`
         -Methods:
          `GET`  used to view rating
          `PUT`  used to edit rating
          `DELETE` used to delete a rating

Once user is logged in, form to submit a rating becomes available. Rating (star number submittion must be filled in and the feedback field is optional) Once submitted, user will see their rating as an additional object to the list view. If user uses the id from the object and follows current URL with `/id` they can access rating detail view where if authorised (ie. ratings 'is_owner' field =true) they will be able to edit/delete the rating. The rated_user field has been set to read only in detail view to avoid repetition when editing.

### Features left to implement

In the future I would like to add additional model for potential buyers and seller to communicate privately so that they could exchange private details there and arrange further details of transaction. I initially added private message to Offers model however as I wanted to make everything but the message available to all users based on `isAuthorisedOrReadOnly` permissions I decided to remove the message. 

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

## Technologies

### Tools and technologies

* Visual Studio Code - used to develop the website
* Github - used to host source code and deploy on Github Pages
* Git- used to commit and push code 
* Python - used as the main language to code the logic of the page
* Django==4.2.8 - framework used
* djangorestframework==3.14.0 - framework used
* Heroku - to deploy the app 
* [dbeaver](https://dbeaver.com/) - used to generate the ER Diagram

### Imports

#### Installed packages

* cloudinary==1.37.0 - media managment cloudinary
* dj-database-url==0.5.0  - Django utility allows to utilize DATABASE_URL environment variable to configure Django application
* dj-rest-auth==2.1.9  - Drop-in API endpoints for handling authentication securely in Django Rest Framework. Works especially well with SPAs (e.g., React, Vue, Angular), and Mobile applications.
* django-allauth==0.44.0  - authentication in django allowing user to sign- up/ sign-in/log-out
* requests-oauthlib==1.3.1 - installed with the allauth above
* django-cloudinary-storage==0.3.0 - cloudinary storage
* psycopg2==2.9.9 - additional dependency needed to support PostgreSQL when deployed to heroku 
* Pillow==10.1.0  - image processing capibilities
* asgiref==3.7.2  - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI. 
* gunicorn==21.2.0
* django-cors-headers==4.3.1  - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
* django-filter==23.5 - installed to use djangofilterbackend
* django-hitcount==1.3.5 - installed to implement page views for adverts
* django-humanize==0.1.2 and humanize==4.9.0 - installed to use naturaltime
* django-money==3.4.1 and py-moneyed==3.0  - used to insert currency
* django-taggit==5.0.1 - used to add tags to adverts
* djangorestframework-simplejwt==5.3.1  - JSON Web Token authentication plugin for DRF.

Installed as dependencies with another packages:
* oauthlib==3.2.2
* PyJWT==2.8.0
* python3-openid==3.2.0
* sqlparse==0.4.4
* urllib3==1.26.16
* pytz==2023.3.post1

## Testing

### Validator Testing

#### Python

No errors shows when passing each file through [CI Python Linter](https://pep8ci.herokuapp.com/)

Each python file in this repo has been run through and each file received the same success message:

![python_validator_check](https://res.cloudinary.com/dmod5eglu/image/upload/v1706145438/python_success_jlmp1o.png)

Couple warnings 'Too long lines of code' when running:
- settings.py (as per image below)

I tried multiple ways to split the lines but unable to deploy then. These are lines of code that have been auto generated. Warnings shown:

![python_validator_check_warnings](https://res.cloudinary.com/dmod5eglu/image/upload/v1706459903/PYTHON_VALIDATOR_vqsjqy.png)

### Manual Testing

#### Functional Testing
 All functions have been manually tested to make sure each function works as intended and only for users as intended. Testing of the entire full stack application can be found within [FRONT-END REPO](https://github.com/AsiaWi/snap-it-up-frontend/)

##### Negative Testing
 All functions have been tested to make sure no functions are availabale to unauthorised users etc. This was done throughout the entire development process. Full application testing can be found on [FRONT-END REPO](https://github.com/AsiaWi/snap-it-up-frontend/)

### Automatic Testing

#### Unit Testing

Unit tests have been performed to check Profile and Advert models.

* Links to test files can be found here:

[PROFILE](https://github.com/AsiaWi/snap-it-up-backend/blob/main/profiles/tests.py)

[ADVERT](https://github.com/AsiaWi/snap-it-up-backend/blob/main/adverts/tests.py)

* Tests outcome when run ``python manage.py test``

![Python_UNIT_TESTS](https://res.cloudinary.com/dmod5eglu/image/upload/v1706146715/python_unittests_wn3ls7.png)


## Bugs

As mentioned within [Validator section](#validator-testing)
![python_validator_check_warnings](https://res.cloudinary.com/dmod5eglu/image/upload/v1706459903/PYTHON_VALIDATOR_vqsjqy.png)

## Deployment

### Version Control

* Git 
    Code has been pushed with git commands to remote repository on Github with commands:

   `` git add .`` - to add files ready to commit

   ``git commit -m "message"`` - to commit the code to local 
    repository ready to be pushed

   ``git push`` - final command used to push commited code to remote repo on Github

### Deploying in Heroku 

* The project has been deployed on Heroku as follows:
     * Use: ``pip freeze > requirements.txt`` to add external libraries to deployed app.
     * Create Heroku account ( step by step guide [here](https://coding-boot-camp.github.io/full-stack/heroku/deploy-with-heroku-and-mysql))
     * In the top right, click 'New'
     * Click 'Create new app'
     * Give your app a name and select your region from drop down 
     * Click 'Create new app' 
     * Go to 'settings' tab, it's important you do it before deployment
     * Scroll down to 'config vars' section and key:
        - ALLOWED_HOST : add url to your heroku app link
        - CLIENT_ORIGIN : frontend heroku url which will be making requests to this API 
        - CLIENT_ORIGIN_DEV: local front-end url
        - CLOUDINARY_URL: 'API key to your cloudinary account'
        - DATABASE_URL : 'URL from your database account'
        - SECRET_KEY: 'Generate your own secret key'
        - DISABLE_COLLECTSTATIC: set to '1'
     * Scroll down to 'Buildpacks' section
     * Click 'Add buildpack'
     * Add Python as first dependency and select 'Save changes'
     * Add node.js as a second dependency and save again
     (This is settings section done)
     * Select 'Deploy' tab at the top
     * Select ' Github' from 'Deployment method'
     * type the name of how you called project in Github and click 'search'
     * Scroll down and select manual deployment method
     * Auto method has also been selected to allow the project to update every time i push the code from Gitpod
     * You can now click to view the app ready and running

### CLONING THE REPOSITORY

1. On Github navigate to repository
2. Click "Code" a green button shown right above the file list
3. Copy the URL of the repo using HTTPS, SSH OR Github CLI
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory
6. Type git clone, and then paste the URL you copied earlier
7. Press enter to create local Clone

For more details on how to clone the remote repo in order to create a local copy for own use, please click [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)


### FORKING

1. On Github navigate to repository
2. click "Fork" located towards the top right corner
3. Select "owner" for the forked repo, from the dropdown menu under "owner" Under "Owner"
4. It will create forked repo under the same name as orinial by default but you can type a name in "Repository name" or add a description in "Description" box.
5. Click "Create fork" !

Forking allows you to make any changes without affecting original project. You can send the suggestions over by submitting pull request. Project owner can review the pull request before accepting the suggestions and merging them.

For more details on how to fork the repo, in order to for example suggest any changes to the project you can click [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo) 

When you have fork to a repository you don't have access to files locally on your device, for this you will need to clone the forked repo.

## Credits

- Code Insitute's DRF walkthrough
- All the links below to help me with creating average rating for list and detail views:
    - [When()](https://docs.djangoproject.com/en/4.2/ref/models/conditional-expressions/)
    - [F()](https://docs.djangoproject.com/en/5.0/ref/models/expressions/)
    - [Stack overflow](https://stackoverflow.com/questions/68953258/%20how-to-calculate-average-of-some-field-in-django-models-and-send-it-to-rest-api) 
    - [django fun](https://django.fun/qa/16172/)
