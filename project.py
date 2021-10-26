#' Simple local Spotify™
#' DS: Gavin South
#' Instructions:
#'   Run everything, then main(). The program is intuitive and will guide you after that.
# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# SQL stuff

# My login
# AXGHY
# others
# PXYWO
# OHXLB

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
#  Libraries
import sqlite3
import string
import random
from playsound import playsound # Note: playsound(, False) if you want to do things while playing song. 

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# Users : ALL WORKING

class user:
    def __init__(self, connection):
        self.u_id = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
        print("What is your first name: \n") 
        self.fname = input("  -> ")
        print("What is your last name: \n") 
        self.lname = input("  -> ")
        print("What music genre do you like: \n") 
        self.genre = input("  -> ")
        print("Out of these songs, type the number of the one you like most: \n")
        music_library(connection)
        self.fav_song = input("  -> ")
        
def create_new_user(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_profiles (u_id TEXT, fname TEXT, lname TEXT, genre TEXT, fav_song INT)")
    new = user(connection)
    values = (new.u_id, new.fname, new.lname, new.genre, new.fav_song)
    cursor.execute("INSERT INTO user_profiles VALUES (?,?,?,?,?)", values)
    print("\nThank you", new.fname, new.lname)
    print("Your new login id name is", new.u_id, "don't forget it.")
    print("\nNow please, type in that id to sign in and start.")
    connection.commit()
    return(new)

def user_menu(current_user, connection):
    print("""    Profile Options:
        1. Print your current info
        2. Edit your current info
        3. View all users
        4. Delete profile
        5. Main Menu
        """)
    b = input("  -> ")
    if int(b) not in [1, 2, 3, 4, 5]:
        print("\nSorry try choosing again, there was something wrong with your entry.\n")
        menu(current_user, connection)
    elif int(b) == 1: print_current_user(current_user, connection)
    elif int(b) == 2: edit_user(current_user, connection)
    elif int(b) == 3: print_all_users(current_user, connection)
    elif int(b) == 4: delete_user(current_user, connection)
    elif int(b) == 5: menu(current_user, connection)

def print_current_user(current_user, connection):
    print("""        User ID: {uid}
        First Name: {fname} 
        Last Name: {lname}
        Favorite Genre: {fgenre}
        Favorite Song: {fsong_title}, by {fsong_artist}
    """
    .format(
        uid = current_user[0][0],
        fname = current_user[0][1],
        lname = current_user[0][2],
        fgenre = current_user[0][3],
        fsong_title = current_user[0][5],
        fsong_artist = current_user[0][6]))
    user_menu(current_user, connection)

def edit_user(current_user, connection):
    cursor = connection.cursor()
    print("Enter new first name: \n")
    fname = input("  -> ")
    print("Enter new last name: \n")
    lname = input("  -> ")
    print("Enter new genre choice: \n")
    genre = input("  -> ")
    print("Enter new favorite song: \n")
    print_song_list()
    fav_song =  input("  -> ")
    values = (fname, lname, genre, fav_song, current_user[0][0])
    cursor.execute("""UPDATE user_profiles 
                      SET fname = ?, lname = ?, genre = ?, fav_song = ?
                      WHERE u_id = ?""", values)
    connection.commit()
    print("")
    values = (current_user[0][0], )
    cursor.execute("SELECT * FROM user_profiles WHERE u_id = ?", values)
    current_user = cursor.fetchall()
    user_menu(current_user, connection)

def print_all_users(current_user, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT fname, lname FROM user_profiles")
    users = cursor.fetchall()
    print("\t\tAll users:")
    for i in range(len(users)):
        print("\t\t" + users[i][0], users[i][1])
    print("")
    user_menu(current_user, connection)

def delete_user(current_user, connection):
    print("\tWould you like to delete your profile? (Y/N)")
    a = input("  -> ")
    if a in ["Y", "y", "yes", "Yes"]:
        print("\tTo confirm please enter in your User ID")
        b = input("  -> ")
        if b == current_user[0][0]:
            print("\t\tDeleting", current_user[0][1], current_user[0][2] + "'s profile...")
            cursor = connection.cursor()
            u_id = current_user[0][0]
            values = (u_id,)
            cursor.execute("DELETE FROM user_profiles WHERE u_id = ?", values)
            connection.commit()
            main()
    elif a in ["N", "n", "No", "no"]:
        print("")
        user_menu(current_user, connection)
    else:
        print("\tPlease type a Y or N.")
        delete_user(current_user, connection)

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
#' Music Library : ALL WORKING

class song:
    def __init__(self):
        print("Song title: \n") 
        self.title = input("  -> ")
        print("Song artist: \n") 
        self.artist = input("  -> ")
        print("Song file name: \n")
        self.file = input("  -> ")
# Only used for adding music, not part of the script due to .wav files being needed. 
def add_song(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS music_library (
                        song_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        title TEXT,
                        artist TEXT, 
                        file TEXT)""")
    new = song()
    values=(new.title, new.artist, new.file)
    cursor.execute("INSERT INTO music_library (title, artist, file) VALUES (?,?,?)", values)
    connection.commit()

def music_library(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM music_library")
    library = cursor.fetchall()
    print("\t\tAll songs:\n")
    print("\t\t", f'{"ID":<5}{"Title":^15}{"Artist":^25}')
    for i in range(len(library)):
        print("\t\t", f'{library[i][0]:<5}{library[i][1]:20}{library[i][2]:<25}')
    print("")

def play_music_library(current_user, connection):
    music_library(connection)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM music_library")
    library = cursor.fetchall()
    print("\t\t• Enter a song number to play: ")
    print("\t\t• Enter 0 to go back to main menu.\n")
    a = input("  -> ")
    if int(a) == 0:
        menu(current_user, connection)
    elif int(a) in range(len(library) + 1):
        print("\n\t\tNow playing:", 
        library[int(a) - 1][1] + ", by",
        library[int(a) - 1][2], "\n")
        playsound("sample_length_music/" + library[int(a) - 1][3])
        play_music_library(current_user, connection)
    else:
        print("\t\tSorry, song number is out of range. Try again.")
        play_music_library(current_user, connection)

def shuffle_music_library(current_user, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM music_library")
    music_library = cursor.fetchall()
    l = list(range(len(music_library)))
    random.shuffle(l)
    for i in l:
        print("\n\t\tNow playing:", 
        music_library[i - 1][1] + ", by",
        music_library[i - 1][2], "\n")
        playsound("sample_length_music/" + music_library[i - 1][3])
    menu(current_user, connection)

def search_song(current_user, connection):
    cursor = connection.cursor()
    print("Search for songs by artist: ")
    a = input("  -> ")
    values = (a, )
    cursor.execute("""SELECT *
                      FROM music_library b
                      WHERE artist = ?""", values)
    results = cursor.fetchall()
    if len(results) == 0:
        print("\nSorry, no songs by that artist in the library.")
        menu(current_user, connection)
    else:
        print("\n\t\tPlaying music by, " + a)
        for i in range(len(results)):
            print("\n\t\tNow playing:", 
            results[i - 1][1] + ", by",
            results[i - 1][2], "\n")
            playsound("sample_length_music/" + results[i - 1][3])
        menu(current_user, connection)
            

# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# Display Menu : Working
def menu(current_user, connection):
    print("""
    1. Music library
    2. Shuffle music library
    3. Search for song
    4. Profile info & preferences
    5. Quit
    """)
    a = input("   -> ")
    if int(a) not in [1, 2, 3, 4, 5]:
        print("\nSorry try choosing again, there was something wrong with your entry.\n")
        menu(current_user, connection)
    elif int(a) == 1: 
        play_music_library(current_user, connection)
        menu(current_user, connection)
    elif int(a) == 2: shuffle_music_library(current_user, connection)
    elif int(a) == 3: search_song(current_user, connection)
    elif int(a) == 4: user_menu(current_user, connection)
    elif int(a) == 5:
        connection.close()
        exit()


# ——————————————————————————————————————————————————————————————————————————————————————————————————————— ####
# Main : Working
def main():
    connection = sqlite3.connect('dbo.db')
    print("""
    Welcome to ________ music player.
    • If you are new here and don't have a saved profile enter the word 'new'. 
    • If you have set up a profile in the past, please enter your five letter id name.
    • If you want to leave enter Q.
    """)
    a = input("  -> ")
    if a in ["new", "New", "NEW", "knew", "nw", "neww"]:
        create_new_user(connection)
        main()
    elif a in ["Q", "q", "Quit", "quit"]:
        exit()
    else: 
        cursor = connection.cursor()
        values = (a, )
        cursor.execute("""SELECT a.u_id, a.fname, a.lname, a.genre, a.fav_song,
                                 b.title, b.artist
                          FROM user_profiles a
                          LEFT JOIN music_library b
                              ON a.fav_song = b.song_id
                          WHERE u_id = ?""", values)
        current_user = cursor.fetchall()
        if len(current_user) == 0:
            print("\nCan't seem to find your profile, try again.")
            main()
        print("Welcome", current_user[0][1], current_user[0][2])
        menu(current_user, connection)

# Calling to get going...
main()
