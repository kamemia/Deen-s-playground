import json

file= open("Anime.Json").read()
data = json.loads(file)

def anime():
    for details in data:
    # print(details)
    
        genres = details.get('genres')
        title = details.get('title')
        studio = details.get('studio')
        rating = details.get('hype')
        desc = details.get('description')
        return details    
    
def recommend():
    
    pref = input("Would you like to watch based on genre, studio or anime rating?\n(Select One): ")
    if pref == "genre":
        genre= input("Input genre prefference: \n")
        print()
        if genre :
            print()
    
recommend()    