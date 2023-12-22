

# Modules

import replit
import time
import random



# Introduction

print("Welcome to Aldar Land")
print("\n")
print("The rules of this RPG adventure is pretty simple.... LIVE")
print("\n")
print("Throughout this adventure you will have many options to choose from which leads to many new dangerous pathways into your story. You will have a starting health of 100, but be careful, if your health gets to 0 it's GAME OVER. You will also have an inventory which will hold all your supplies, each time you pick up an item your inventory will update as well as when you pass a new level. Keep in mind, you will get chances to use your tools you've gathered sometime in the story.")

print("\n")

# What is your Name

name = input("Before we begin, what would you like your name to be: ")

print("Excellent choice",name)

time.sleep(3)

replit.clear()

# Intro to story
print("The treasure of Aldar has been missing for years! The king of Aldar lost it when he was travelling through a sand storm. A group of thiefs stole it along with a weapon that can control its power! They have hidden it somewhere but rumours have arised that the thiefs are keeping it in a secret base! Multiple people including you have enrolled to find it. This treasure posesses a power that can give people extraordinary powers if they have bonded with the treasure. Whoever finds the treasure will get paid very well.")
enter = input("Click enter to clear the page")
replit.clear()

print("It's 7 AM in the morning, and you're riding out in the desserts of Aldar. You and your horse have been travelling for days, seeking to find the long lost treasure of Aldar.")
print("\n")
print("You can barley see anything from all the sand going in your face.")
print("\n")
print("Suddenly you hear a cry for help. You turn around and see that a person is injured. They sound like they're in pain.")
print("\n")

# inventory and variables

inventory = ["watch","book","water","piece of bread","10 dollars","map"]

health = 100

item2 = ""

helpp = True

fighting = ""

transpo = ""

puzzle1 = True

interrogation_damage = True

interrogation_damage2 = True


# All of the def statements for the RPG

# arrival def statement

def arrival():
  print("You have arrived to Aldar town")

# inventory def statement

def i1():
  i = input("Enter i to check your inventory.")

  if (i == "i"):
    print(inventory)
    print("\n")
    print(name+": Looks like everythings there..... Ugh my face is all bruised up, I have to go back to Aldar town")

    enter = input("Click enter to fast-forward to Aldar town")

  while (i != "i"):
    i1()
    i = "i" # breaks the while loop



# Level 1

def level1():
  global health, helpp

  # displays inventory

  print("Here is your starting inventory:",inventory)
  print("\n")

  # Do you want to help the person?

  help_person = int(input("Would you like to help the injured person: The options are 1 (yes) 2 (no) or 3 (wait) "))

  # Help the injured person

  if (help_person == 1):
    helpp = True
    replit.clear()
    print("You rush towards the person, you get off your horse and see that the injury is fake. ")
    print("\n")
    print(name+": What th-")
    print("\n")
    print("The person knocks you out cold.")
    print("\n")
    
    # Decrease in health

    health = health - 10
    
    print("Your health is now",health)
    enter = input("Click enter to continue")
    replit.clear()
    
    print("You wake up and see that the thief is attempting to ride the horse, but ultimatly fails and gets thrown off.")
    print("\n")
    print(name+": Hey!")
    print("\n")
    print(name,"Runs to the thief and confronts him")
    print("\n")
    print(name+": Come here!")
    print("\n")
    print("Before",name,"can reach the thief he had ran away but you managed to get back your stuff")
    print("\n")

    i1()
 
    replit.clear()

    time.sleep(3)
    
    arrival() # Welcome to Aldar town
    time.sleep(3)

   

  # Don't help the injured person

  elif (help_person == 2):
    helpp = False
    replit.clear()
    print(name,"rides away from the injured person as he has to keep looking for the treasure")
    print("\n")
    print(name+": There can't be any distractions.")
    print("\n")
    print("(20 minutes later)")
    print("The sandstorm is only getting worse.",name,"holds up the map to see but sand keeps getting in the eyes.")
    print("\n")
    print(name+": There's no way I can continue with this severe sandstorm. I have to go back to Alder town to get some new supplies and maybe some shut eye.")
    print("\n")
    

    enter = input("Click enter to fast-forward to Aldar town")

    replit.clear()
    time.sleep(3)

    arrival() # Welcome to Aldar town
    time.sleep(3)

  # Wait....

  while (help_person == 3):
    replit.clear()
    time.sleep(3)
    level1()
    help_person = 2 # breaks the while loop

  # user doesn't pick a valid choice

  while (help_person > 3 or help_person < 1):
    replit.clear()
    time.sleep(1)
    print("Not a valid option")
    level1()
    help_person = 3 # breaks the while loop

# level 2 defs

def shirt1():

  # What shirt would you like?

  shirt = int(input("Which shirt do you want: 1 (blue shirt) 2 (green shirt) or 3 (keep the same shirt)"))

  # If you want the blue shirt

  if (shirt == 1):
    replit.clear()
    print("You've decided to go with the blue shirt")

  # If you want the green shirt

  elif (shirt == 2):
    replit.clear()
    print("You've decided to go with the green shirt")

  # If you want to keep your dirty shirt

  elif (shirt == 3):
    replit.clear()
    print("You've decided to keep your dirty shirt.")

  # If user hasn't entered a valid option

  while (shirt > 3 or shirt < 1):
    replit.clear()
    time.sleep(1)
    print("Not a valid option.")
    shirt1()
    shirt = 3 # breaks the while loop

# Which item do you want def statement

def item1():
  global item2 # global statement for item2

  item = int(input("Which item would you like to take: 1 (axe) 2 (doll) or 3 (water bottle)"))

  # If user chose the axe

  if (item == 1):
    print("You have chosen to take the axe")
    inventory.append("axe")
    print("Here is your updated inventory")
    print("\n")
    print(inventory)
    item2 = "axe"
    enter = input("Click enter to clear the page")
    replit.clear()

  # If user chose the doll

  elif (item == 2):
    print("You have chosen to take the doll.")
    inventory.append("doll")
    print("Here is your updated inventory")
    print("\n")
    print(inventory)
    item2 = "doll"
    enter = input("Click enter to clear the page")
    replit.clear()

    
  # If user chose the watter bottle

  elif (item == 3):
    print("You have chosen to take the water bottle. Why take an extra water bottle?")
    inventory.append("Water bottle")
    print("Here is your updated inventory")
    print("\n")
    print(inventory)
    item2 = "Water bottle"
    enter = input("Click enter to clear the page")
    replit.clear()

      
  # When no valid option is chosen

  while (item > 3 or item < 1):
    print("\n")
    print("Not a valid option")
    item1()
    item = 1 # breaks the while loop


# Level 3 updated health

def updatehp():
  
  if (helpp == True):
    health = 90
    health = health - 10
    print("Your health is now",health)
              
  else:
    health = 100
    health = health - 10
    print("Your health is now",health)


# Level 3 fighting the ravangers

def fighting():
  print("To damage the ravanger answer the question correctly!")

  fight = int(input("The ravanger goes for a punch with his right hand what should you do: 1 (try to punch him) 2 (dodge it) 3 (stay still)"))

  # If user chooses to punch

  if (fight == 1):
    print("The ravanger knocks you out before you can punch him")

  # If user chooses to dodge it

  elif (fight == 2):
    print("You dodge the ravangers punch and hit him back, you stand up and see ZOLA with an impressed face. Suddenly a ravanger comes behind you and knocks you out cold. Isn't it freezing up in here?")

  # If user chooses to stay still

  elif (fight == 3):
    print("The ravanger is not impressed and knocks you out")

  # If user has not picked a valid option

  elif (fight > 3 or fight < 1):
    print("You answered incorrectly, the ravanger knocks you out.")

# level 3 transportation

def transport1():
  global transpo # global statement for transportation

  transportation = int(input("Which transportation do you want to take 1 (foot), 2 (horse)"))

  # If user chooses to go on foot

  if (transportation == 1):
    transpo = "foot"
            
    print("You've decided to go on foot")
    time.sleep(3)
    replit.clear()
    print("You and Jeffery safley store your horses and begin to follow the ravengers")
    print("\n")
    print("You follow them for a solid 15 minutes until they stopped at czeko village.")
    print("\n")
    print(name+": Czecko village? What do they want from there?")


    print("\n")
    print("You then spot a man speaking to ZOLA")
    print("\n")
    print("Jeffery: What are they saying?")
    print("\n")
    print("You then see the strange man hand over a map to ZOLA.")
    print("\n")
    print(name+": Is that th-")
    print("\n")
    print("Jeffery: The map to the treasure. I hope not.")
    print("\n")


    print(name+": We have to go in the village.")
    print("\n")
    print("Jeffery: Alright")
    print("\n")
    print("You both head into the village, you walk quitley and hide behind some hay. You now have a better view of what's happening.")
    print("\n")
    enter = input("Click enter to clear the page")
    replit.clear()
    print("(Sinister music playing)")
    print("ZOLA: hmmm, you've done well, I will give you 3 percent of the treasure we find. That's if you live...Ravengers, deal with him.")
    print("\n")

    # Def for attacking the ravanger    
    def attackrav():
      
      # Do you want to attack?

      attack = int(input("NO, they're hurting the poor person. Do you want to attack: 1 (attack) 2 (No) 3 (Ask them nicley to stop)"))

        
      global item2

      # If user chooses to attack

      if (attack == 1):
        print(name+": HEY!")
        print("\n")
        print("The ravengers start to charge towards you")

        # If user chose the axe then they can use it during this battle

        if (item2 == "axe"):
          print("You grab some thing random out of your inventory and coincidentally grab your axe.")
          print("\n")
          print("You throw the axe onto the charging ravenger and the ravenger gets injured. Aren't you glad you brought your axe.")
          inventory.remove("axe")
          print("Your inventory is now",inventory)
          print("\n")

          # Global statement for health and helpp

          global health, helpp 

          print("Another ravanger gets extremely mad and tackles you over. Jeffery tries to help but he becomes unconscious.")
          print("\n")
          fighting()

        # If user chose the doll then they can use it during this battle

        elif (item2 == "doll"):
          print("You grab something random out of your inventory and find yourself holding the doll you took from Jeffery. You throw the doll at the Ravanger but nothing happens. Jeffery gets second hand embrassment.")
          print("\n")
          print("Jeffery: Really?! You took the doll instead of the Axe!?")
          inventory.remove("doll")
          print("You inventory is now",inventory)
          print("\n")
          print("Another ravanger gets extremely mad and tackles you over. Jeffery tries to help but he becomes unconscious.")
          fighting()
          
          
        # If user chose water bottle then they can use it during this battle

        elif (item2 == "Water bottle"):
          print("You grab something random out of your inventory and find yourself holding the extra water bottle you took from Jeffery. Out of panick you throw the water bottle at one of the ravengers and it bounces off their head.")
          print("\n")
          print("ZOLA: Hmm, you amuse me")
          inventory.remove("Extra water bottle")
          print("Your inventory is now",inventory)
          print("\n")
          print("Another ravanger gets extremely mad and tackles you over. Jeffery tries to help but he becomes unconscious.")
          fighting()
          
        
        updatehp()
        enter = input("Click enter to continue")
          
       # If you choose to not attack

      if (attack == 2):
        print("You've decided to not attack.")
        print("\n")
        print("Jeffery: What are we waiting for!")
        print("\n")
        print(name+": Wait Jeff NO!")
        print("\n")
        print("Jeffery: HEY!")
        print("\n")
        print("The ravangers take down Jeffery easily, and come charging towards you. Out of panick you froze which led the ravengers to knock you out.")
            
        updatehp()
        enter = input("Click enter to continue")

      # If you choose to ask them nicley to stop

      elif (attack == 3):
        print(name,"stood up and said")
        print("\n")
        print(name+": Hello.")
        print("\n")
        print("The ravangers beating up the old man are in awkward silence")
        print("\n")
        print("Random ravanger: Sir?")
        print("\n")
        print("ZOLA: Who are you?")
        print("\n")
        print(name,"is extremly nervous and says.")
        print("\n")
        print(name+": Hi",name,"I'm ZOLA...")
        print("\n")
        print("Jeffery face palms himself")
        print("\n")
        print(name+": I was just wondering if you guys can lay off him, you know? But trust me I say this with a kind intention.")
        print("\n")
        print("ZOLA: Hmm, explorers, take them!")
        print("\n")
        print("Ravangers swarm around you and with a BANG, you've been knocked out.")
        updatehp()
        enter = input("Click enter to continue")

      # While user doesn't pick a valid option

      while (attack > 3 or attack < 1):
        print("\n")
        print("Not a valid option")
        attackrav()
        attack = 3 # breaks the while loop

    attackrav()

      
  # If user chooses to go by horse

  elif (transportation == 2):
    transpo = "Horse"
    print("You've decided to go by horse")
    print("\n")
    print("You and Jeffery follow the Ravangers and ZOLA with your horses. Your trying your best to be quiet. The sand keeps getting worse but you still manage to be behind them. Suddenly one of the horses steps on a cacti")
    print("\n")
    print("Horse: Knarr")
    print("\n")
    print("The ravangers hear this sound and turn around. ZOLA spots the both of you and yells...")
    print("\n")
    print("ZOLA: GET THEM!")
    print("\n")
    print(name+": Oh no")
    print("\n")
    print("Jeffery: We have to go now!")
    print("\n")
    print(name+": What about the horse?")
    print("\n")
    print("Jeffery: We have to leave it")

    # Leave horse behind def statement

    def leave1():
      leave = int(input("Leave the horse behind: 1 (yes) 2 (no) 3 (fight off the ravangers)"))

      # If user leaves the horse

      if (leave == 1):
        replit.clear()
        print(name+": I'm sorry buddy")
        print("\n")
        print("Jeffery and",name,"run as fast as they can but the ravangers are very fast.")
        print("\n")
        print("Jeffery: What are they eating to be able to run so fast!")
        print("\n")
        print(name,"is getting really tired. Out of exaustion",name,"falls down and hits a rock!")
        print("\n")
        print("Jeffery:",name+"?",name+"!")
        print("\n")
        print("The ravangers catch up to",name,"and Jeffery and capture them.")

        updatehp()
        enter = input("Click enter to continue")
      
      # If user doesn't leave the horse (loyal)

      elif (leave == 2):
        replit.clear()
        print(name+": No! I won't leave my horse behind.")
        print("\n")
        print("Jeffery: You also have to make everything hard for yourself don't you!")
        print("\n")
        print("At this point the ravangers are close to them.")
        print("\n")
        print("Jeffery: Wasn't expecting to be captured this soon after what happened last year!")
        print("\n")
        print(name+": We'll be fine.")
        print("\n")
        print("The ravangers arrive to Jeffery and",name,"and knock them out COLD. It's freezing up in here do ya think?")

        updatehp()
        enter = input("Click enter to continue")
      
      # If user decides to fight the ravangers

      elif (leave == 3):
        replit.clear()
        print(name+": I'll fight them before they can even think of getting close to my horse!")
        print("\n")
        print("Jeffery: Wha-")
        print("\n")
        print("(FYI Jeff think's your delusional)")
        print("\n")
        print(name,"acting like Captain America and all sprints towards the ravangers. Wait, Captain America doesn't exist in the 1800s.... oh well.")
        print("\n")
        print("Before",name,"can reach the ravangers",name,"trips and falls on the head....BLOP")
        print("\n")
        print("No one can replace Captain America")
        print("\n")
        print("There is an awkward silence between Jeffery and the ravangers.")
        print("\n")
        print("Jeffery: I'm not with him.")

        updatehp()
        enter = input("Click enter to continue")
      
      # While user doesn't pick valid options

      while (leave > 3 or leave < 1):
        print("Not a valid option")
        leave1()
        leave = 3 # breaks the while loop
    
    leave1()
      


        
  # While user doesn't pick valid options

  while (transportation > 2 or transportation < 1):
    print("Not a valid option.")
    transport1()
    transportation = 2 # breaks while loop

# Level 4 decrease in health for Interrogation
def interro():

  global health # global statement for health

  health = health - 20
  print("ZOLA didn't like your answer. Your health has gone down to",health)
  print("\n")
  print("ZOLA: Since you won't comply let's try something else.")

# Level 4 interrogation part 1


def interrogation():
  global interrogation_damage # global statement for interrogation_damage

  # King Aldar sent you didn't he?

  interro1 = int(input("ZOLA: King Aldar sent you didn't he: 1 (Not just us, anyone who enrolled will get paid if they find the treasure) 2 (No) 3 (Why do you care)"))

  # If user picks yes

  if (interro1 == 1):
    print("ZOLA: Hmmm, just as I expected.")

    print("\n")

    interrogation_damage = False

    interrogation1()
      
  # If user picks no

  elif (interro1 == 2):
    interro()
    interrogation_damage = True
    interrogation1()
    
  # If user talks back to ZOLA

  elif (interro1 == 3):
    interro()
    interrogation_damage = True
    interrogation1()

  # While user doesn't pick valid choice

  while (interro1 > 3 or interro1 < 1):
    print("Not a valid option")
    time.sleep(3)
    interrogation()
    interro1 = 3 # breaks the while loop

# Level 4 interrogation part 2
def interrogation1():

  global interrogation_damage2 # global statement for interrogation_damage2

  interro2 = int(input("ZOlA: Say you managed to escape this wonderful cell, what would you do: 1 (I'll come after you) 2 (I won't tell anybody about you) 3 (I'll tell King Aldar that I've found you) 4 (Don't answer)"))

  # If user picks 1

  if (interro2 == 1):
    interro()
    interrogation_damage2 = True

  # If user picks 2

  elif (interro2 == 2):
    print("ZOLA: Will you now?")
    print("\n")
    print("ZOLA knows your lying. You are lying right?")

    interrogation_damage2 = False

  # If user picks 3

  elif (interro2 == 3):
    interro()
    interrogation_damage2 = True

  # If user picks 4

  elif (interro2 == 4):
    interro()
    interrogation_damage2 = True

  # While user doesn't pick valid option

  while (interro2 > 4 or interro2 < 1):
    print("Not a valid option")
    print("\n")
    interrogation1()
    interro2 = 3 # breaks the while loop

  
  print("\n")    
  print("ZOLA: Now, for the final question, do you know what this is. (ZOlA pulls out a golden map)")
  
  # Do you know what this golden map is?

  interro3 = int(input("Do you know what this is: 1 (yes) 2 (lie no)"))

  # If user chooses yes

  if (interro3 == 1):
    print(name+": Yes, the map to the treasure of Aldar")

  # If user chooses no

  elif (interro3 == 2):
    print(name+": No, what is that?")
    print("\n")
    print("ZOLA: This right here is the map to the treasure of Aldar. I got it from an infromant at Czecko village.")
  
  # While user hasn't picked a valid option

  elif (interro3 > 2 or interro3 < 1):
    print("Not a valid option")
    print("\n")
    print("ZOLA: huh?....I'll take that as a no.")
    print("\n")
    print("ZOLA: This map is the map that leads me to the treasure of Aldar. I got it from an informant at Czecko village.")
    interro3 = 2 # breaks the while loop
  
  # level 4 questions def

def question1():
  question = int(input("What do you want to ask ZOLA: 1 (why do you want the treasure) 2 (where is Jeffery) 3 (what do you want from us)"))

  # If user asks 1

  if (question == 1):
    replit.clear()
    print(name+": Why do you want the treasure?")
    print("\n")
    print("ZOLA: Why do you? Assuming that you do want it too. You're explorers out in the dessert so, of course you're looking for it too.")
    print("\n")
    print(name+": We want the treasure so we can return it to it's rightfull owner, your taking it to abuse it's power.")
    print("\n")
    print("ZOLA: A little bit out of context here. I am the treasures rightfull owner. A long time ago the people of Aldar took it away from me.")
    print("\n")
    enter = input("Click enter to clear the screen")
    replit.clear()
    print(name+": Thats not true")
    print("\n")
    print("ZOLA: But it is.")
    print("\n")
    print(name+": How? Why?")
    print("\n")
    print("ZOLA: Once the people of Aldar saw it's power they knew they had to take it from me. But then it got stolen hahaha")
    print("\n")
    print(name+": The people of Aldar aren't monsters like you, they probabaly had a good reason.")
    print("\n")
    print("ZOLA: If only you knew the truth about the people of Aldar and the horrors of Aldar land.")

  # If user asks 2

  elif (question == 2):
    replit.clear()
    print(name+": Where's Jeffery!")
    print("\n")
    print("ZOLA: Relax, we've done nothing to him.")
    print("\n")
    print(name+": Lies where is he!")
    print("\n")
    print("ZOLA: You really don't take me for my word....classic Aldarian move.")
    print("\n")
    print(name+": What's that meant to mean?")
    print("\n")
    enter = input("Click enter to clear the screen")
    replit.clear()
    print("ZOLA: Aldarians are not to be trusted.")
    print("\n")
    print(name+": Alarians aren't to be trusted... what about you? You and your ravangers. How are we supposed too trust you. ")
    print("\n")
    print("ZOLA: Well I have provided you with a five star room to take you as hostage")
    print("\n")
    print("(The room is actually really garbage)")

  # If user asks 3

  elif (question == 3):
    replit.clear()
    print(name+": What do you want from us!")
    print("\n")
    print("ZOLA: What do we want from you? Haha...")
    print("\n")
    print("(That was a weird laugh)")
    print("\n")
    print("ZOLA: You came storming in our backyard, getting in our business.")
    print("\n")
    enter = input("Click enter to clear the screen")
    replit.clear()
    print(name+": No, you're going have a dangerous treasure and no madman should be able to wield it.")
    print("\n")
    print("ZOLA: Very humourous, we don't want anything to do with you, you're just an obstacle in our path.")
    print("\n")
    print("ZOLA: But there are some things I would like to know.")


  # While user hasn't picked a valid option

  while (question > 3 or question < 1):
    print("Not a valid option")
    time.sleep(3)
    replit.clear()
    question1()
    question = 3

# Level 5 Defs

# Tools def

def tool():
  tools = int(input("Which tool would you like to take to help you escape: 1 (stick) 2 (ink) 3 (glass)"))

  # If user picks 1

  if (tools == 1):
    replit.clear()
    print("You push the chair across the room to get to the stick, but you and the chair your tied to end up falling.")
    print("\n")
    print(name+": Ughhhhhh")
    time.sleep(1)
    print("You have failed")
    time.sleep(3)
    tool()
    tools = 0
  
  # If user picks 2

  elif (tools == 2):
    replit.clear()
    print("You attempt to take the ink behind you but end up falling on your head.")
    print("\n")
    print(name+": THIS CANT BE HAPPENING!!!")
    time.sleep(1)
    print("You have failed")
    tool()
    tools = 0
  
  # If user picks 3

  elif (tools == 3):
    replit.clear()
    print("You move your chair to the shelf but can't reach the glass. You then come up with the idea to push your chair to the wall to break it.")
    print("\n")
    print(name+": Come on!")
    print("\n")
    print("After seven tries you finally get the chair to break.")
    print("\n")
    print(name+": YES!")
    print("\n")
    print("Although your hands are tied you still manage to grab the glass from the shelf")
    print("\n")
    
    enter = input("Press any key or click enter to cut the rope.")
    print("\n")
    print("Try one more time.")
    print("\n")
    enter = input("Press any key or click enter to cut the rope.")
    print("\n")
    print("ONE MORE TIME!!!!!!!!")
    print("\n")
    enter = input("Press any key or click enter to cut the rope.")
    print("\n")
    print(name+": YES! It worked.")
    time.sleep(3)
    
  
  # If user doesn't pick a valid option

  elif (tools > 3 or tools < 1):
    print("Not valid")
    time.sleep(3)
    tool()
    tools = 3 # breaks the while loop
    

    

# Def for Math door
def math_lesson():
  value = int(input("Enter a value to add"))
  value2 = int(input("Enter another value to add"))
  sum1 = int(input("Enter the sum of the two numbers"))
  replit.clear()

  equation = value + value2 

  if (equation == sum1):
    print("\n")
    print("The door has opened")

  else:
    print("\n")
    print("You're terrible at math")
    print("\n")
    print("Please try again, that was terrible")
    time.sleep(5)
    math_lesson()

# Def for english door


def english_lesson():
  global puzzle1

  sentence = input("Enter anything that contains at least one letter from the first 3 letters of the alphabet")
	 
  
  if ("a" in sentence or "b" in sentence or "c" in sentence):
    while (puzzle1 == True):
      print("The door has opened")
      puzzle1 = False
      
          
  else:
    print("Invalid")
    time.sleep(3)
    replit.clear()
    english_lesson()

# Level 6 defs

# level 6 fighting ZOLA part 1 def

def fightzz2():
  global health # global statement for health

  fightz2 = int(input("What do you do: 1 (punch) 2 (kick him) 3 (Do a backflip then punch)"))

  # If user chooses 1

  if (fightz2 == 1):
    print("You punch ZOLA. ZOLA is now hurt!")
    print("\n")
    print("ZOLA get's really mad and punches you back.")
    health = health - 10
    print("\n")
    print("Your health is now",health)
    print("\n")
    print("You try striking ZOLA again")
    strike = int(input("What should you do: 1 (punch again!) 2 (Push him)"))

    # If user chooses 1

    if (strike == 1):
      print("You try punching ZOLA but he has blocked it.")
    
    # If user chooses 2

    elif (strike == 2):
      print("You push ZOLA")

    # While user doesn't pick valid option

    while (strike > 2 or strike < 1):
      print("You have not inputted a valid option, due to this ZOLA attacks you.")
      time.sleep(3)
      strike = 2
    
    
  # If user chooses 2

  elif (fightz2 == 2):
    print("You kick ZOLA. Unfortunatly, you have a weak leg.")
    print("\n")
    print("ZOLA gets his powers back and obliterates you.")
    print("\n")
    print("You have died")
    fightzz2()

  # If user chooses 3

  elif (fightz2 == 3):
    print("You attempt to do a backlip but ultimatly fail and fall on your back.")
    print("\n")
    print("You have died.")
    time.sleep(5)
    fightzz2()

  # If user doesn't pick a valid option

  while (fightz2 > 3 or fightz2 < 1):
    print("Not a valid option")
    time.sleep(3)
    fightzz2()
    fightz2 = 3 # breaks the while loop
  
  

# level 6 dodging ZOLA's beams

def fightzo():
  fightz = int(input("What should you do 1 (stay still) 2 (dodge it by going right) 3 (Try to slide under the beam)"))

  # If user chooses 1

  if (fightz == 1):
    print("The beam of energy oblitarates you.")
    print("\n")
    print("You have died")
    print("\n")
    print("But don't worry, you will respawn very quickly to the nearest check point.")
    enter = input("Click enter to restart")
    replit.clear()
    fightzo()
  
  # If user chooses 2

  elif (fightz == 2):
    print("You dodge it by going to the right.")
  
  # If user chooses 3

  elif (fightz == 3):
    print("You slide under the beam but end up right under ZOLA. ZOLA punches you in the face and you die.")
    fightzo()
  
  # While user doesn't pick a valid option

  while (fightz > 3 or fightz < 1):
    print("Not a valid option")
    time.sleep(3)
    replit.clear()
    fightzo()
    fightz = 3 # breaks the while loop

# level 6 fighting ZOLA part 2

def fightzo1():
  
  fightz1 = int(input("What do you want to use 1 (watch) 2 (book) 3 (water bottle) 4 (piece of bread) 5 (10 dollars) 6 (map) or 7 (note)"))

  # If user picks 1

  if (fightz1 == 1):
    print("You throw the watch at ZOLA and it hits his head, he barley gets injured.")
    inventory.remove("watch")
    print("\n")
    print("Here is your updated inventory")
    print(inventory)

  # If user picks 2

  elif (fightz1 == 2):
    print("You throw the book at ZOLA and it hits his head, he has moderate pain in the head.")
    inventory.remove("book")
    print("Here is your updated inventory")
    print(inventory)

  # If user picks 3

  elif (fightz1 == 3):
    print("You throw the water bottle at ZOLA and it hits his head, he has no pain.")
    inventory.remove("water")
    print("Here is your updated inventory")
    print(inventory)

  # If user picks 4

  elif (fightz1 == 4):
    print("You throw the piece of bread at ZOLA and it doesn't even hit him, what a waste of food.")
    inventory.remove("piece of bread")
    print("Here is your updated inventory")
    print(inventory)

  # If user picks 5

  elif (fightz1 == 5):
    print("You throw the money at ZOLA and it doesn't even hit him, he has no pain.")
    inventory.remove("book")
    print("Here is your updated inventory")
    print(inventory)

  # If user picks 6

  elif (fightz1 == 6):
    print("You throw the map at ZOLA and it doesn't even hit him. ZOLA feels no pain.")
    inventory.remove("map")
    print("Here is your updated inventory.")
    print(inventory)

  # If user picks 7

  elif (fightz1 == 7):
    print("You throw the note at ZOLA but he doesn't get injured")
    inventory.remove("note")
    print("Here is your updated inventory")
    print(inventory)

  # While user doesn't pick valid option

  while (fightz1 > 7 or fightz1 < 1):
    print("Not a valid option")
    time.sleep(3)
    replit.clear()
    fightzo1()
    fightz1 = 7

# Final Choice of The Game Def Statement

def final_choice1():
  final_choice = int(input("WARNING THIS DECISION WILL AFFECT YOUR ENDING 1 (take the treasure) 2 (save Jeffery) or 3 (WAKE UP!)"))

  # User takes the treasure

  if (final_choice == 1):
    replit.clear()
    print("You rush off to take the treasure off of ZOLA. But then you look back and see that the pyramid has collapsed on Jeffery!")
    print("\n")
    print(name+": NOOOOO! JEFFERY!!!!")
    print("\n")
    print("ZOLA: Hahahaha....fool. You lost your only friend!")
    print("\n")
    print("Out of rage you bond with the treasure and fire ZOLA.")
    print("\n")
    print("ZOLA: Wait WAIT NOOOOO")
    print("\n")
    print("You rush off to Jeffery")
    print("\n")
    print(name+": Jeffery! Jeff! Are you alright!")
    print("\n")
    enter = input("Click enter to clear the page")
    replit.clear()
    print("You check to see his pulse.....")
    time.sleep(5)
    print("He's gone")
    time.sleep(5)
    replit.clear()
    print("5 hours later")
    print("\n")
    print(name,"is sitting down still in shock.")
    print("\n")
    enter = input("Click enter to clear the screen")
    replit.clear()
    print(name+": No one deserves to have this treasure! Not even king Aldar himself!")
    print("\n")
    print("You rush off to your horse and ride far away until you think it's safe. You near a ocean and get off your horse.")
    print("\n")
    print(name+": This treasure has caused enough trouble!")
    print("\n")
    print(name,"then throws the treasure down the ocean.")
    print("\n")
    print(name+": Now no one will ever get it.")
    print("\n")
    print(name,"then rides away with his horse.")
    print("\n")
    print("(What a terrible ending, notice how you never questioned who I am. Guess you chose wrong.)")
    enter = input("Click enter to clear the screen")
    replit.clear()
    print("CREDITS")
    print("\n")
    print("Coded by: Abdelrahman Abdelaal")
    print("\n")
    print("Produced by: Replit")
    print("\n")
    print("Taught by: Mr. Zoratti")
  
  # User saves Jeffery

  elif (final_choice == 2):
    replit.clear()
    print("You rush off to Jeffery and manage to push him away from the collapsing pyramid")
    print("\n")
    print("ZOLA: HAHAHA, fool. You should've taken the treasure.")
    print("\n")
    print("(Oh No!)")
    print("ZOLA: Now you'll pay")
    print("\n")
    print("ZOLA emits a large beam at you and Jeffery")
    enter = input("Click enter to clear the screen.")
    replit.clear()
    print("("+name+"! Jeffery!)")
    print("\n")
    print("(Where are you guys)")
    print("\n")
    print("(You can't leave me! I narrated your story!)")
    time.sleep(10)
    replit.clear()
    print("(I don't want to be alone.)")
    print("\n")
    print("(I guess this is the end.)")
    print("\n")
    print("(Oh boy this is like an Avengers Infinity war ending....even worse...)")
  
  # User WAKES UP!

  elif (final_choice == 3):
    replit.clear()
    print("Suddenly you see a bright light shining at you. You open your eyes....")
    time.sleep(5)
    print("\n")
    print("Mr. Zoratti: Abdelrahman? Are you paying attention? Have you been sleeping?")
    print("\n")
    print("Abdelrahman: I just came up with the best idea for culminating!")
    print("\n")
    print("Mr. Zoratti: But we just started the course.... I barley even introduced you to turtle")
    print("\n")
    print("Abdelrahman pulls out his laptop and starts coding and coding.")
    print("\n")
    enter = input("Click enter to clear the screen")
    replit.clear()
    print("Mr. Zoratti: Hey this isn't apropriate!")
    print("\n")
    print("Abdelrahman then stops typing and showed Mr. Z the finished code.")
    print("\n")
    print("Mr. Zoratti: That's the most beautiful game I've ever seen. You know what, I'll make an exception, when culminating comes you can hand this code in.")
    print("\n")
    print("9 weeks later")
    print("Mr. Zoratti: Wow, that was amazing")
    print("\n")
    enter = input("Click enter to clear the screen")
    replit.clear()

    # Enter a mark until it's 100!

    mark = int(input("Enter a mark:"))
    while (mark < 100):
      print("Too low")
      mark = int(input("Enter a mark:"))
    
    if (mark >= 100):
      print("Perfect!")
    
    print("This explains as to who the narrator is, it was Abdelrahman! And the plot holes must've because it was a dream all along!")
  
  while (final_choice > 3 or final_choice < 1):
    print("NOT VALID THIS IS A VERY IMPACTFUL QUESTION!")
    time.sleep(5)
    final_choice1()
    final_choice = 3 # breaks the while loop



# The output


# level 1 - The helpless person

level1()

# Level 2 - Aldar town

replit.clear()

# Interaction between user and Jeffery

print(name,"walks to Jeffery house where he can give some supplies.")

print("\n")

print(name+": Jeffery!")

print("\n")

print("Jeffery: Wow, you look disgusting. That's what happens when you try to look for the treasure of Aldar without me.")

print("\n")

print(name+": Yea......I need supplies")

print("Jeffery: Of course you do, I'll only give you supplies ONLY if you let me come with you next time you go looking for the treasure.")

print("\n")

print(name+": Really....")

print("\n")

print("Jeffery: Yup")

print("\n")

print(name+": Wow, real mature Jeff.....fine.")

print("\n")

print("Jefferson: Alright, go choose your supplies upstairs. Maybe even grab a new shirt for yourslf")

print("\n")

print(name,"walks upstairs and goes to the closet first.")

# Shirts

shirt1()

print(name,"Then heads to jeffery's supply room.")

print("\n")

print("You enter the room and see an axe, a doll, and a water bottle.")

# items

item1()


# level 3 - Enter ZOLA

# Plot for level 3

replit.clear()
print("After having taken some supplies, you and jeffery ride out to the dessert the next day")
print("\n")
print(name+": Here's where I got to yesterday")
print("\n")
print("Jeffery: Looks like you didn't get too far")
print("\n")
print(name+": Hahah very funny")
print("\n")
print("Jeffery: Quick take cover!")
print("\n")
print("Jeffery quickly drags",name,"to cover and they hide")
print("\n")
print(name+": What is it?")
print("\n")
print("Jeffery: It's the ravengers, and their leader, ZOLA. They've been after the same treasure as us. They're willing to do anything to get to the treasure first.")
print("\n")
enter = input("Click enter to clear the screen")
replit.clear()
print(name+": What happens if they do?")
print("\n")
print("Jeffery: The power the treasure holds is too strong, if they get it, they'll abuse the power. I know they will")
print("\n")
print(name+": That means we have to go after them.")
print("\n")
enter = input("Click enter to clear the page")
replit.clear()
print("Jeffery: Yes we must, but the question is, do we follow them by horse or by foot?")

# Transportation

transport1()

# Level 4 - Interrogation

replit.clear()
print("FIVE HOURS LATER")
time.sleep(3)
replit.clear()

# Plot for level 4

print("After five long hours you finally wake up.")
print("\n")
print("You open your eyes and realize your not at home. You had realized, the ravangers had kidnapped you. You look around but see that Jeffery isn't with you.")
print("\n")
print("The door infront of you opens and there you see ZOLA.")
print("ZOLA: Well, well, well. You're finally awake. Took you awhile. Your friend Jeffery really tried to fight his way out.")
print("\n")

# If user picks horse then gets the item he chose removed because it was used if user pick to by foot

if (transpo == "Horse"):
  print("ZOLA: Oh and by the way, we found a",item2,"in your inventory. You won't be needing that.")
  print("\n")
  print("ZOLA throws away the",item2,"you got from Jeffery.")
  inventory.remove(item2)
  print("\n")
  print("Your inventory is now",inventory)

# Ask questions
question1()

print("ZOLA: Now, it's time for me to ask the questions.")
print("\n")
print("ZOLA: But before we continue, I suggest you drink this.")
print("\n")
print("ZOLA hands you a red drink. You don't want to drink it but you fear you must.")
print("\n")
print("You drink it and your health increases to 100.")
print("\n")
print("(what?! why would they want your health to be 100?)")
print("\n")

print("* NOTE ZOLA will now interrogate you. There will be a series of questions that he will ask you, if he doesn't like your answer you will get your health damaged. *")

# Health assignment

health = 100

print("\n")

enter = input("Click enter to continue")

replit.clear()

# ZOLA interrogates you!

interrogation()

print("ZOLA: According to this map, we are halfway from the destination. Soon we will get the treasure, and hold such a power that'll make us unstoppable.")
print("\n")
print("ZOlA: Now, I'll leave you here while we go get the treasure. And when we come back, you'll see that it was all worth it.")

enter = input("Click enter to clear the screen")

# Level 5 - escape plan

# Plot for level 5

replit.clear()
print("(Two hours later)")
print(name+": I can't sit here and do nothing!, I have to find a way to break out of this 'five star room hostage room'. ")
print("\n")
print(name+": Lets see is there anything around the room that can help me break this rope.")
print("\n")
print("You look around the room and end up finding three objects. A random stick on the floor across the room, ink for a pen behind you but also on the floor right behind your chair, or a piece of glass on a shelf.")
print("\n")
print("Note: In this level you will be introduced to checkpoints, if you choose a option that leads to failure you'll be respawned to the checkpoint")
print("\n")

# Which tool do you choose?

tool()

replit.clear()
print("You get yourself out of the rope and open the door")
print("\n")
print("(Why would they leave the door open like that? Reckless ravangers)")
print("\n")
print("You get outside the hostage room and find yourself in a hallway. You see a door infront of you and try to open it")
print("\n")
print(name+": Why won't this open?!....What th-")
print("\n")
print("'Please enter a correct math equation to open this door.'")
print("\n")
print("How do they have this tech in the 1800s?")
print("\n")
print(name+": What did ZOLA put in that drink?")
print("\n")
print("'We will first begin with an addition equation'")
print("\n")

# Math door

math_lesson()

print("You walk in and see another door.")
print("\n")
print(name+": You're going to pay ZOLA")
print("\n")
print(name+": What does this door want now?")
print("\n")
print("Please type anything that has at least one letter from the first 3 letters of the alphabet ")
print("\n")

# English door

english_lesson()
time.sleep(3)
replit.clear()
print("You open the door and see that it's Jeffery")
print("\n")
print("(audience claps)")
print("\n")
print("(Wait hows there an audience)")
print("\n")
print(name+": I don't know")
print("\n")
print("(Did you just speak?)")
print("\n")
print(name+": I mean.. Jeffery!")
print("\n")
print("Jeffery:",name+"?")
print("\n")
print(name+":I'm gonna get you out don't worry.")
print("\n")
print("You untie Jeffery.")
enter = input("Click enter to clear the screen")
replit.clear()
print("\n")
print("Jeffery: Ugh, they gave me some weird red juice")
print("\n")
print(name+": Yea, same here..... But there's no time, we have to go to ZOLA now!")
print("\n")
print("Jeffery: What do you mean?")
print("\n")
print(name+": He's going to the treasure of Aldar and by now he's nearly there")
print("\n")
print("Jeffery: But we don't even know where the treasure is!")
print("\n")
print(name+": There has to be some clues here as to where they went. Let's look around.")
print("\n")
enter = input("Click enter to clear the screen.")
print("\n")
replit.clear()
print("\n")
print("You walk across another hall and find a door.... this time it actually opens by itself.")
print("\n")
print(name+": Finally! Normal doors!")
print("\n")
print("You enter a room that looks like as if it's a planning room. You look around and find a written note saying the exact location of where ZOLA is going.")
print("\n")
print("(Ok now this is too easy! The user probably doesn't even want to play anymore from all these plot holes.)")
print("\n")
print(name+": Jeffery I know where they're going!")
print("Jeffery: Great! What are we waiting for!")
print("\n")
print(name+": Let's do this!")
print("\n")
print("(avengers theme plays)")
print("\n")
enter = input("Click enter to clear the screen")
replit.clear()

# level 6 - finale
print("THE FINALE")
print("\n")
print("You and Jeffery get outside of ZOLA head quarters and find your horses locked up in cages.")
print("\n")
print(name+": Hey look it's our horses! Looks like they got them with us!")
print("\n")
print("You and Jeffery run to your horses.")
print("\n")
print(name+": How long has it been? 5 hours? Feels like forever.")
print("\n")
print("Before riding onto your horses here's an update on your health")

# Update on your health and inventory

if (interrogation_damage == True and interrogation_damage2 == False):
  health = 80
  print("Your health is at",health)

elif (interrogation_damage == False and interrogation_damage2 == True):
  health = 80
  print("Your health is at",health)


elif (interrogation_damage == True and interrogation_damage2 == True):
  health = 60
  print("Your health is at",health)


elif (interrogation_damage == False and interrogation_damage2 == False):
  health = 100
  print("Your health is at",health)

print("\n")
inventory.append("note")

print("Here's the updated version of your inventory",inventory)

print("NOTE in this level you will be given the option to use one of your materials. Good luck....oh no! He's waking up!")
time.sleep(3)
print("(What? Who's waking up? No matter, carry on. I'll get to the bottom of this.)")
enter = input("Whenever you're ready to face ZOLA, click enter.")
replit.clear()

# Level 6 plot

print("4 HOURS LATER")
print("\n")
print("You and Jeffery have been riding out in the dessert for 4 hours. You look down at the note you've found and it says strailway holse. Jeffery yells out and says.")
print("\n")
print("Jeffery: Look! We made it to strailway holse.")
print("\n")
print(name+": That's where the treasure will be, let's move.")

print("You and Jeffery put your horses aside to a safe space. You look up and see a pyramid.")
print("\n")
print("Jeffery: I got a bad feeling about this.")
print(name+": There's no time for that. We're the only people stopping ZOLA from having ultimate power.")
print("You and Jeffery climb the pyramid. You see a strange and dark entrance.")
print("\n")
print("Jeffery: That's totally not creepy")
print("\n")
print("You and Jeffery enter the pyramid. The first thing you see is a unconcious ravanger.")
print("\n")
print(name+": What happened here")
print("\n")
enter = input("Click enter to clear the screen")
replit.clear()

print("Suddenly the ravanger wakes up.")
print("\n")
print("Ravanger: ZOLA....H-....He bet-.....He betrayed us. The power of the treasure was too strong. It turned him into a-")
print("Jeffery: A what")
print("\n")
print("Ravanger: a-")
print(name+": What is it?")
print("\n")
print("Ravanger: A monster.")
enter = input("Click enter to clear the screen")
replit.clear()

print("The ravanger dies.")
print("\n")
print("Jeffery: ZOLA's a monster now?!")
print(name+": We have to face him before he gets any stronger.")
print("\n")
print("You and Jeffery continue to walk inside and see more ravanger bodies. You then see something glowing.")
print("\n")
print("Jeffery: What th-")
print("\n")
print("ITS ZOLA")
print("\n")
print("ZOLA: Hey! Looks like you made it to the party. You see what I was talking about. Look at this power, it's incredible")
print("\n")
print(name+": What did you do")
print("\n")
print("ZOLA: I bonded myself with the treasure. Look at what happened!")
print("\n")
print("Jeffery: Yeah well your gonna need to unbond, like really quickly.....or else we'll just have to-")
print("\n")
print("ZOLA: Do what? Haha what are you gonna do?")
print("\n")
print(name+": We're gonna kick your butt off to Czecko village.")
print("\n")
print("ZOLA: Let's see then shall we.")

enter = input("Click enter to clear the screen")
replit.clear()

print("Jeffery charges towards ZOLA but gets pushed away and is unconcience.")
print("\n")
print("(What a way to get rid of a side character am I right?)")
print("\n")
print("ZOLA faces you, he charges up his hand and releases a beam of energy towards you")

# Dodging ZOLA's beam
fightzo()

print("ZOLA looks tired from shooting that beam. Nows your chance. What do you want to use from your invetory to damage ZOLA.")

# Fighting ZOLA
fightzo1()

print("ZOLA: You can't stop me, even if you try your hardest.")
print("Due to ZOLA being tired from emitting a large beam. Instead he emits a smaller non life threatning but can damage your health beam.")
print("\n")
print("ZOLA emits a beam at you.")

print(name+": AGH")
enter = input("Click enter to clear the screen")
replit.clear()
# Decrease in health

if (interrogation_damage == True and interrogation_damage2 == False or interrogation_damage == False and interrogation_damage2 == True):

  health = 80
  
  health = health - 5
  print("Your health is now",health)

  print("\n")
  print("ZOLA: Your too weak to stop me!")
  print("ZOLA fires another beam but you manage to dodge it. Now ZOLA is really tired. ZOLA tries to fire another beam but he can't. You rush towards ZOLA")
  
  fightzz2()
  print("ZOLA pushes you which makes you fall on the ground. ZOLA then drags you and drops you down the pyramid stairs")
  print("\n")
  health = health - 20
  print("Your health is now",health)
    

# Decrease in health

elif (interrogation_damage == True and interrogation_damage2 == True):

  health = 60

  health = health - 5
  print("Oh no! Your health is at",health)

  print("\n")
  print("ZOLA: Your too weak to stop me!")
  print("\note")
  print("ZOLA fires another beam but you manage to dodge it. Now ZOLA is really tired. ZOLA tries to fire another beam but he can't. You rush towards ZOLA")

  fightzz2()
  print("ZOLA pushes you which makes you fall on the ground. ZOLA then drags you and drops you down the pyramid stairs")
  print("\n")
  health = health - 20
  print("Your health is now",health)

# Decrease in health

elif (interrogation_damage == False and interrogation_damage2 == False):

  health = 100

  health = health - 5
  print("Your health is at",health)

  print("\n")
  print("ZOLA: Your too weak to stop me!")
  print("\n")
  print("ZOLA fires another beam but you manage to dodge it. Now ZOLA is really tired. ZOLA tries to fire another beam but he can't. You rush towards ZOLA")

  fightzz2()

  print("ZOLA pushes you which makes you fall on the ground. ZOLA then drags you and drops you down the pyramid stairs")
  print("\n")
  health = health - 20
  print("Your health is now",health)

print("While your getting your butt beat by ZOLA Jeffery finally wakes up.")
print("\n")
print("Jeffery: What happened?",name+"?")
print("\n")
print("Jeffery then looks outside and sees you getting beat up by ZOLA.")
print("\n")
print("Jeffery: What can I use here to help",name,"out?")
print("\n")
print("Jeffery looks around and finds a un-bonding machine.")
print("\n")
print("Jeffery: Woah")
print("\n")
print("Jeffery takes the machine and aims it at ZOLA")
print("\n")
print("Jeffery: Look out",name+"!")
print("\n")
print("ZOLA see's Jeffery and then fires a beam at the roof of the pyramid. It's going to collapse on Jeffery if you don't rescue him. But on the other hand, the treausre is un-bonding with ZOLA, you can take the treasure that way ZOLA won't have his powers before it's too late.")

# FINAL CHOICE

final_choice1()
print("\n")

for i in range(1,11):
  print("Hope you enjoyed!")
  time.sleep(1)
