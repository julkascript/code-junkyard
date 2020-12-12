# Available at https://code-junkyard.tk/

My final project for the project defense for SoftUni. It's built on Django + JS + Bootstrap/HTML/CSS (DB - PostgreSQL). Hosted on AWS, deployed with Docker.

## Purpose:
Code Junkyard is a place for "recycling" code. Have you ever abandoned a project that contains loads of quality code? One man's trash is another man's treasure! We have to start caring about the code environment. Let's not pollute GitHub and other platforms with rusty and forgotten code. Let's start recycling and reusing code!

On the yard you can post code snippets or even whole files. It doesn't need to be great because most of the times the idea itself is more than enough. It's right about time for some treasure hunting!

## How do I run it?
Follow these steps if you would like to locally clone the project.
Django, Python and PostgreSQL are necessary for running the project.

1. Navigate to a directory of your choice and open your git bash there (or navigate through CMD with cd directory path).
2. Run the command .git clone https://github.com/julkascript/code-junkyard
3. Open the code_junkyard folder with your IDE. Then pip install virtualenv.
4. After that run the following command in the same directory you are at the moment: virtualenv venv. This will create venv folder for your virtual environment.
5. Then navigate through the terminal to venv/Scripts. Now run activate.bat. This will run your virtual environment. 
6. Navigate back (cd) to the main folder.
7. Run pip install -r requirements.txt
8. Configure python interpreter for the project (options available from your IDE).
9. Check in the code_junkyard/settings.py file for the database details.
10. Create your database (its name and password should be identical to the settings file).
    1. NOTE: Check if the templates folder is selected as one for the project. You can set it up manually from the IDE.
11. Run the server. 
12. Run the following command in the terminal: manage.py makemigrations
13. Run the following command in the terminal: manage.py migrate
14. The project is fully set-up and ready for use.


## Site functionalities:

1. Navigation bar (available at all times) with path to home, displaying sign in/up options for guests and profile/sign out options for logged in users and a footer with link to my GitHub. 
2. Home page (welcome page) displaying info about the site, as well as some posts previews at the bottom. If you open a post from this page you will be asked to log in (if you already are not logged) and then you will be redirected to the post you chose.  
3. Sign in/Sign up functionality.
4. Private parts access restriction for guest users. The user needs to sign in in order to view the other parts of the site.
5. Admin panel and admin account for the admin. Can access everything.
6. Posts.
    1. Posts can be viewed by everyone but edited only by the creator.
    2. Post list page. Displays all posts.
    3. Post create page. Creates post. Every post has a creator, title, description, picture and etc.
    4. Post display page (when post is opened). 
    5. Post edit page.
7. Profile - profiles can be viewed by everyone but edited only by the profile user.