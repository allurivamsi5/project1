Task-1 PostgreSQL
1. Fisrtly, create an account on heroku.
2. Secondly, created an app name and then click on "Configure Add-ons".
4. In the “Add-ons” section of the page, type in and select “Heroku Postgres.”
5. Now, click the “Heroku Postgres :: Database” link.
6. On your database’s overview page, click on “Settings”, and then “View Credentials.”
7. This is the information you’ll need to log into your database.
8. You can access the database via Adminer, filling in the server (the “Host” in the credentials list), your username (the “User”), your password, and the name of the database, all of which you can find on the Heroku credentials page.


Task-2 Python and Flask

1. Fisrtly, installed pip on terminal and check it by running pip in a terminal window.
2. Extract the project1 zip file.
3. In a terminal window, navigate into your project1 directory.
4. Run pip3 install -r requirements.txt in your terminal window.
5. Set the environment variable, on Windows, the command is instead set FLASK_APP=application.py. You may optionally want to set the environment variable FLASK_DEBUG to 1, which will activate Flask’s debugger and will automatically reload your web application whenever you save a change to a file.
6. Set the environment variable DATABASE_URL to be the URI of your database.
7. Run flask run to start up your Flask application.
8. If you navigate to the URL provided by flask, you should see the text "Project 1: TODO"!
