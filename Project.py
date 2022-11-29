#Automating my manga read list
#First to list all the manga I have not read or finished

from random import shuffle
import random
from secrets import choice
import time


print("Hello there,Welcome to my manga recommender :)")

manga  =[ 'Akumetsu', 'Black clover', 'Dandadan', 'Dorehedoro', 'Fire Punch', 'Jagaaan', 'Asura', 'Kingdom', 'Mashle', 'Monster', 'Record of Ragnarok ', 'GOH', 'Vagabond', 'Tokyo Revengers']

#time to let the algos decide
#print(choice(manga))

#lets kick it up  a notch shall we?
#we will group them into manhua and manga , started and never touched based on my read history

Seinen = ['Kingdom', 'Monster', 'Record of Ragnarok', 'Tokyo Revengers', 'GOH', 'Dorehedoro', 'Asura']
Shonen = ['Jagaaan', 'Mashle', 'Akumetsu', 'Predator', 'Boxer', 'Red Storm', 'Dandadan']
Hentai = "I AM DISSAPOINTED IN YOU!"
Isekai = ['Trash Hero', 'Jobless Reincernation','Slime']
genre = ['Shonen', 'Seinen', 'Hentai', 'Isekai']
feel = print("Fancy a read? ")
def reccomend():

      #print('What do you feel like reading? ', genre) 
      print(genre)
      mood = input('What do you feel like reading? ')

      if mood == "Shonen":
         print(choice(Shonen))

      elif mood == "Seinen":
         print(choice(Seinen))

      elif mood == "Hentai":
         print(Hentai)

      else: 
         print(choice(Isekai))     

   
      print("Have fun! :)")

reccomend()

Seinen.append("Death Note")

Retry = input("Would you like to try again?, Press Y if yes: ")

if Retry == "Y":
      reccomend()
else:
   print("Goodbye")
   