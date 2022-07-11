# AriseandShine_CC

This repository contains django code that delivers the <a href="https://www.ariseandshinecc.org">Arise and Shine Care Center</a> web application.

You can follow this README alongside <a href="https://docs.djangoproject.com/en/3.1/">official django docs</a>. and <a href="https://simpleisbetterthancomplex.com/tutorial/2016/10/14/how-to-deploy-to-digital-ocean.html">simple is better than complex tutorials</a>

[![Django CI](https://github.com/google-boy/AriseandShine_CC/actions/workflows/django.yml/badge.svg)](https://github.com/google-boy/AriseandShine_CC/actions/workflows/django.yml)

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
  
## Step 4: Clone this repostory

- clone the repostory in the virtual env
- pip install -r requirements.txt. This install all the project requirements including django,

## Step 5: Application secrets

Create an .env file on the app root directory. Copy the contents of .env.example to .env file you just created.
Edit the information according to your application configuration.

## Step 6: Create superuser

Create a supperuser for Site admin login by running the following command on the terminal or command prompt.
Follow the prompts, remember you won't see your password as you type.

    python manage.py createsuperuser

## Future improvements

- Serve admin site from a different subdomain e.g admin.ariseanshinecc.org using django-host or any other appropriate lib.
- Writing unit tests.
