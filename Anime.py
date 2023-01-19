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
            genre = choice.get('genres')
            title = choice.get('title')
            desc = choice.get('description')
            if pick == studio:
                print(studio,genre,title,desc)
                
    # categorize rating
    if pref == "genre":
        print("-----------Still in Dev--------------")
        gen = input("Genre: \n")
        for opt in data:
            slct = opt.get('genres')
            print(slct)
            # match if gen is in range of element in list(slct)                
                
recommend()            
    
   