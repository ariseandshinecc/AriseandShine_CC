# AriseandShine_CC

This repository contains django code that delivers the www.ariseandshinecc.org web application.

## Requirements

 - Python 3.6+,
 - PostgreSQL 10+,
 - Python Virtualenv(optional).
 
## Step 1: Installations

  - Make sure Python3.6+ is installed on your OS
  - Install PostgreSQL 10+
  
## Step 2: Database Configuration
  - Create a database and user, Grant all permisions to this user on this database.
 
## Step 3: Virtualenv

  - Create a python virtual enviroment in a directory where you want your project to live.
  - Activate the virtual environment.
  
## Step 4: Clone this repostory.

  - git clone https://github.com/google-boy/AriseandShine_CC.git in the virtual env
  - pip install -r requirements.txt. This install all the project requirements including django,

## Step 5: Sensitive data

  - Create an .env file to store this kind of information
    
      - SECRET_KEY=
      - DEBUG=
      - DATABASE_URL=

## Future improvements

    - Serve admin site from a different subdomain e.g admin.ariseanshinecc.org using django-host or any other appropriate lib.