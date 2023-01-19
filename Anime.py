import json
import random
file= open("Anime.Json").read()
data = json.loads(file)

def recommend():
    pref = input("Would you like to watch based on genre, studio or anime rating?\n(Select One): ")
    if pref == "studio":
        print("----------You know your stuff----------")
        pick= input("Studio Name: \n")
        for choice in data:
            studio = choice.get('studio')
            genre = choice.get('genres')
            title = choice.get('title')
            desc = choice.get('description')
            rating = choice.get('hype')
            if pick == studio:
                print("Studio Name:",studio," Genres:",genre,"Name:",title,"Description",desc,"Rating",rating, "\n")
            
    if pref == "genre":
        print("-----------Use One genre--------------")
        pick = input("Genre: \n")
        for opt in data:
            genre = opt.get('genres')
            studio = opt.get('studio')
            title = opt.get('title')
            desc = opt.get('description')
            rating = opt.get('hype')
            genres = genre[::]
            if pick in genres:
                print("Studio Name:",studio," Genres:",genre,"Name:",title,"Description",desc,"Rating",rating, "\n")
                        
    # categorize rating
                
recommend()            
    
   