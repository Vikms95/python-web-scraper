import sqlite3
import imdb
from imdb.parser.sql import get_movie_data
from imdb.utils import analyze_title


# ----------------------------------- Declaration functions to connect with DataBase----------------- #

def light_connect(function):
    def int_function():

        connectVar = sqlite3.connect("F:\_PRO\_PROJECTS\webscrappertut2\basedatos.sqlite3")
        cursorVar = connectVar.cursor()

        function(connectVar,cursorVar)
    
    return int_function

def connect():
    def create_file():
        
        connectVar = sqlite3.connect("F:\_PRO\_PROJECTS\webscrappertut2\basedatos.sqlite3")
        cursorVar = connectVar.cursor()

        cursorVar.execute(f'''CREATE TABLE ACTORS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR (20)
            BIRTHYEAR INTEGER)''')

        connectVar.close()

@light_connect
def insert_file(connection,cursor):

    actorInfo = get_actor_info(get_actor_ID())

    cursorVar.execute("INSERT INTO ACTORS VALUES(NULL,?,?)",(
        actorInfo.keys()[0],
        actorInfo.values()[0],
    ))

# -----------------------------------  Declaration functions to retrieve and store data ----------------------------------- #

def get_actor_ID(): # (completed/commented for testing) Finds a requested actor at the IMBd database and returns actor ID as a string
    
    ia = imdb.IMDb()

    # Asks to input person name and surname and stores it

    #actor_to_search = input('Actor/actress name and surname: ')
    #actor_to_search = list(actor_to_search.split())
    #actorName, actorSurname = actor_to_search[0], actor_to_search[1] 
    
    # Searches on IMBd database and stores name and birth year
    
    actorSearch = ia.search_person(f"Emma Watson") # (momentary)
    #actorSearch = ia.search_person(f"{actorName} {actorSurname}")
    actorSearch = actorSearch[0]
    actorID = actorSearch.personID

    return actorID
    
def get_actor_info(actor_id): # (completed) Gets actor ID as argument and stores his name and birthyear to dictionnary
    
    actorID = actor_id
    actorBirthDate = actorID['birth date']
    actorName = actorID['name']

    actor_data = {actorName: actorBirthDate}

    return actor_data

def get_actor_movies(actor_id): # (completed) Gets actor ID as argument and stores his films to a dictionary (title: movie release year)
    
    ia = imdb.IMDb()

    # (completed) Gets raw list of dictionaries from IMBd

    actorID = actor_id()
    actors_film_dic = ia.get_person(actorID) # actorFilms is dict()
    
    # (completed) Gets films from the actor inside it's database and stores on dictionary
    
    movie_data = {}
    for job in actors_film_dic['filmography'].keys():
        for movie in actors_film_dic['filmography'][job]:
            
            try:
                
                movie_data[movie['title']] = movie['year']

            except KeyError: # 
                
                movie_data[movie['title']] = 'Year not available'

    return movie_data



#ia =imdb.IMDb()
#actorMovies = get_actor_movies(actorID)
#print(get_actor_movies(get_actor_ID))

insert_file()

