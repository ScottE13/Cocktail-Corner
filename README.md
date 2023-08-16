# Cocktail Corner

Developed for educational purposes as part of the Code Institute diploma in web development.

NOTE - (Obviously) Incomplete project however I was advised to submit what I had at this point. I will need to request a break from the course and hope to return and complete this in the future.

- - -

## Project Goals

### User Stories

As an initial user I want to:

- Clearly understand the purpose of the website.
- Navigate around the site with ease.
- View recipies submitted by others.
- Be guided to register an account.
- Register an account easily without providing personal information.

As a returning user I would also want to:

- Be able to log in and out with ease.
- Add recipies of my own to the websie.
- View all of my recipies in one place.
- Edit my recipies.
- Delete my recipies.
  
As an administrator of the website I want to:

- Create, amend and delete categories.
- Add, edit or delete recipies added by users.
  
- - -

## Database Model

An initial database plan was modelled using [dbdiagram.io](https://dbdiagram.io/home)

![Database Model](cocktailcorner/docs/images/database_model.jpg)

- - -

## UX Design

- - -

## Features

- - -

## Technologies

- - -

## Testing

(rough bug notes only)

Bug RuntimeError: Working outside of application context. This typically means that you attempted to use functionality that needed the current application. To solve this, set up an application context with app.app_context(). See the documentation for more information.
Occurred When trying to create the initial database using the models.
Fix  
from app import app, db

app.app_context().push()

db.create_all()

Fix found on [stack overflow](https://stackoverflow.com/questions/34122949/working-outside-of-application-context-flask)

Bug  sqlalchemy.exc.ArgumentError: Error creating backref 'category' on relationship

Occurred Testing initial registration functionality

Fix backref ‘category’ was shared with a data name from the Cocktail model. Renamed the model name from ‘category’ to ‘cocktail_category’

Bug AttributeError: 'NoneType' object has no attribute 'encode' (password.encode)

Occurred Testing initial registration functionality.

Fix  name attribute was missing from html registration form

Bug Could not store hashed password in database.

Occurred Trying to register first user.

Fix Model was set to a max string length of 25 which was not enough to store the hashed password. Updated max length to 250 and re-created the database.

Bug DataError
sqlalchemy.exc.DataError: (psycopg2.errors.InvalidTextRepresentation) invalid input syntax for integer: "userone"

Occured trying to add first cocktail to database because the site tracks the username in the session and not the user.id which is the foreign key in the models

Fix was to filter and return the id value from the username. Finding the correct syntax was difficult and eventually found it in the sql alchemy docs

- - -

## Deployment

- - -

## References

Cocktail recipes and images used were sourced from the BBC website.

Code insittutes combined taskmanager walktrhough as basis for login/registration code
