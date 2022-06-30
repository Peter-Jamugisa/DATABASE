import csv
from cs50 import SQL
open("final1.db","w").close()
database=SQL("sqlite:///final1.db")
database.execute("CREATE TABLE movies (movies_id INTEGER PRIMARY KEY,title TEXT)")
database.execute("CREATE TABLE genre_movies (movies2_id INTEGER,genres_id INTEGER PRIMARY KEY,FOREIGN KEY (movies2_id) REFERENCES movies(movies_id))")
database.execute("CREATE TABLE genres (genre_id INTEGER PRIMARY KEY,genre TEXT,FOREIGN KEY (genre_id) REFERENCES genre_movies(genres_id))")

with open("gross movies.csv","r") as file:
    reader=csv.DictReader(file)  

    for row in reader: 
        title=row["Film"].strip().capitalize()
        movies_id=database.execute("INSERT INTO movies(title) VALUES (?)",title)
        for Genre in row["Genre"].split(","): 
            genre=Genre.split()
            genre_id=database.execute("INSERT INTO genre_movies(movies2_id) VALUES((SELECT movies_id FROM movies WHERE title=?))",title)
            genre=database.execute("INSERT INTO genres(genre_id,genre) VALUES((SELECT genres_id FROM genre_movies WHERE movies2_id=?),?)",genre_id,genre) 