import json
import random
file= open("Anime.Json").read()
data = json.loads(file)
# use list index 

for details in data:
    stud = details.get('studio')
    genre = details.get('genres')
    title = details.get('title')    
    desc = details.get('description')
    rating = details.get('hype')
 
def recommend():
    pref = input("Would you like to watch based on genre, studio or anime rating?\n(Select One): ")
    if pref == "studio":
        pick= input("Studio Name: \n")
        for choice in data:
            studio = choice.get('studio')
            if studio == pick:
                print(studio,genre,title,desc, rating)
                break
    # categorize rating
    if pref == "genre":
        gen = input("Genre: \n")
        for opt in data:
            for sel in opt['genres']:
                if gen in sel:
                    print(stud,genre,title,desc,rating)
                    break

recommend()            
    
   