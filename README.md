# Overview

Thist short and simple program explores SQLite functionality in a Python enviroment. I recently made a program that played music from a local file and saved user data about preferences using Pandas and CSV files. I updated that code to use SQLite and it works much better due to the ease of use with data base management. 

This program is a music player that is self running and revolves around a single user. When you run it, it will ask for a login and then do a query and join to find the user information associated with that login. Then the program will send the users data and a sql connection throughout the program to do different tasks. Like; updating profile info, deleting profiles, querying music by artist name, and other SQL related functionality. 

The reason I decided ot build this program out was to practice database management scripting and to try using those functions without propeer MySQL interface for example. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

Im using a relational SQLite database I appropriately named `dbo`
The database has two tables:

`TABLE music_library (song_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT,  file TEXT)`

`TABLE user_profiles (u_id TEXT, fname TEXT, lname TEXT, genre TEXT, fav_song INT)`

These tables can be joined on a common variable which is the song indexes primary key. 

# Development Environment

> Sqlite3 for DataBase managment
Playsound Library
Random character generator

> Python 3.7
Microsoft™ Visual Studio Code

# Useful Websites

>[Random Documentation](https://docs.python.org/3/library/random.html)

>[Playsound Documentation](https://pypi.org/project/playsound/)

>[SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)

# Future Work

  [ ] Album art, lyrics, song info? Consider data types in SQL then a django web-app.

  [ ] Display album art. Maybe need to do a django web-app. 