#Imports
from termcolor import colored
import random
import time
import os
import sys
#common = ["Cat Fish(common)", "BlueGill(common)", "Trout(common)", "Tuna(common)", "Anchovy(common)", "Mackeral(common)","Bass(common)", "Cod(common)", "Carp(common)", "Goldie(common)", "Cape Fish(common)", "Arizona Cod(common)"]

#rare = ["Swordfish(rare)", "Flying Fish(rare)", "Squid(rare)","Tron(rare)"]
  
#legendary = ["Tiger Shark(legendary)","Great White Shark(legendary)"]

#mythical = ["Megaladon(Mythical :o)"]

#Routines
def print_slow(str, interval = 0.07):
    for letter in str:
        #print(letter, end='')
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(interval)
    print('')

print_slow(colored("Welcome to Animal Crossing!", "yellow"))
time.sleep(1.5)
name = input(colored("What is your name? ", "green"))
print_slow(colored("Nice to meet you " +name+ "!", "cyan"))
island = input(colored("What should your island be called? ", "red"))
print_slow(colored("Cool name for an island!", "blue"))
time.sleep(1.5)
print_slow("0. Inventory")
print_slow("1. Check Island")
print_slow("2. Meet Villagers")
print_slow("3. Go fish")
print_slow("4. Shop")
print_slow("5. Wardrobe")
print_slow("6. Eat lunch")
print_slow("7. Quit")
time.sleep(1.5)
print_slow(colored("Try visiting your island first!","red"))
time.sleep(1.5)

#More sleep
#time.sleep(1.5)

#Indexed collection (dictionary) of items
inventory = {"stuff": ["old rod"], 
             "food": [], 
             "fish": [],
             "wallet": 0.0}

while True:
  check = random.choice(["\tOh looks like mom got you some food better save that for lunch!","You found some food hooray!", "Hmmm looks like nobody is here :(","\tWow all the villagers came to greet you \n and gave you some supplies to survive! (You obtained a golden fishing rod!)"])
  fish = random.choice(["Cat Fish(common)", "BlueGill(common)", "Trout(common)", "Tuna(common)", "Anchovy(common)", "Mackeral(common)","Bass(common)", "Cod(common)", "Carp(common)", "Goldie(common)", "Cape Fish(common)", "Arizona Cod(common)","Swordfish(rare)", "Flying Fish(rare)", "Squid(rare)","Tron(rare)","Tiger Shark(legendary)","Great White Shark(legendary)","Megaladon(Mythical :o)"])
  
  villagers = random.choice(["You met Alex!","You met Bobby!","You met Mary!","You met Trevor!","You met Baby Boo!","You met Pepe!","You met Lauren!","You met Joey Apples!", "You met your mom!"])
  lunch = random.choice(["salad","sandwich","burger","turkey burger","turkey sandwich","ham sandwich","pasta","cookie","meatball sub","turkey sub"])
  money = random.choice([100, 1000, 1000000212, 0.1, 958.5, 60, 675, 369, 32, 0, 10, 46])
  answer = input(colored("What do you want to do? ","green"))
  if answer == "0" :
    for key, value in inventory.items():
	    print_slow(f"\t{key}: {value}")
  elif answer == "1" :
    print_slow(check)
    if (check.find("golden fishing rod") != -1) :
      inventory["stuff"].append("golden fishing rod")
    elif (check.find("food") != -1) :
      inventory["food"].append("food")  
  elif answer == "2" :
    print_slow(colored("\t"+villagers,"cyan"))
  elif answer == "3" :
    print_slow("\tYou caught "+ fish + "!")
    inventory["fish"].append(fish)
  elif answer == "4" :
    if (len(inventory["fish"]) > 0) :
      del inventory["fish"][0]
    else : 
      money = 0.0
    inventory["wallet"] = inventory["wallet"] + money  
    total = inventory["wallet"]     
    print_slow(f"\tYou got {money:.1f} from selling your fish! Total $: {total:.1f}") 
  elif answer == "5" :
    print_slow(colored("\tYour mom gave you some clothes to put on! Not saying you were naked though....","blue"))
  elif answer == "69":
    print_slow(colored("Wait a second what did you type. Stop breaking the game NOW! That is a BAD number stop it! Phew, at least you do not know what happens when you type 420."))
  elif answer == "420":
    print_slow(colored("Oh god what have you done!?!? Stop this now! You do not know what you have done!"))
    quit()
    time.sleep(1.5)
    print_slow(colored("\tWow you look splendid!","yellow"))
  elif answer == "6" :
    print_slow(colored("\tMom packed you a "+lunch+" for lunch mmmm tasty!","cyan"))
  elif answer == "7" :
    msg = f"\tCongrats! You have collected ${money:.1f}"
    print_slow(colored(msg, "green"))
    break
    #urmom!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
