import os
os.system('clear')

def intro():
    print("""Youre being stalked, choose the choices wisely to escape!
          \nSchools out. You look around at the red and yellow leaves as they fall from the gray gloomy sky. 
          Tonight is Halloween, your parents warned you to come straight home after school,
          you never know what may happen or who's watching you. 
          You start your walk and quickly notice an old van on the side of the road. 
          The windows are oddly tinted to almost pitch black, the van starts, 
          you panic and pick up the paste and to your worst nightmare the van starts to follow.
          \nChoose between the alleyway or the shortcut through the neighbors yard to escape!""")
    
    choice1 = input("Do you  go 'alleyway' or 'shortcut'? ").lower()
    
    if choice1 == 'alleyway':
        endof_alleyway()
    elif choice1 == 'shortcut':
        neighbors_yard()
    else:
        print("Invalid choice. Try again.")
        intro()
        
def endof_alleyway():
    print(""" 
    You make a sharp cut into the alleyway and keep running. You have a moment of 
    relief believing you're out of the van's reach only to hear a car door slam and 
    stepfoots coming down the alley. Quick Run! \n Choose to jump over the wall to escape or
    Hide in the pile of garbageand trash!
    """)
    
    choice2 = input("Do you go 'wall' or 'hide'? ").lower()
    
    if choice2 == 'wall':
        die("You dive over the wall and land on your neck. You snap your spinal cord. You Died.")
    elif choice2 == 'hide':
        van()
    else:
        print("Invalid choice. Try again.")
        endof_alleyway()
        
        
def van():
    print(""" You dive into the pile of garbage and trash, mystery juice and trash is all over you. 
        The noise from the trash causes you to get caught. 
        The tall and solid kidnapper grabs you and puts a bag over your head and you pass out. 
        You wake up with chains on your feet and a big lock to keep you secure. 
        Something falls out of your shirt, a piece of a fork from the trash, perfect thing to help you escape. 
        You pick the lock and break free. \n What will you choose  Distract the driuver or Jump out the van
        """)
    
    choice = input("Do you go 'distract' or 'jump'? ").lower()
    
    if choice == 'distract':
        win("You take the lock to the drivers head causing a crash. You escape with minor injuries.")
    elif choice == 'jump':
        die("You jump and roll. As you roll the other cars on the road zoom bye and crush ur head. You Died")
    else:
        print("Invalid choice. Try again.")
        van()   
        
        
def neighbors_yard():
    print(""" You push through the gate.
          And with a sigh of relief you stop and catch your breath,
          which is short lived because you hear the dogs barking and 
          growling immediately. \n What will you do now? Jump the fence or Run into the woods?""")
    
    choice4 = input("Do you go 'woods' or 'fence'? ").lower()
    
    if choice4 == 'woods':
        die("As youre running through the woods you trip over a branch and the dogs rip you limb from limb. You Died. ")
    elif choice4 == 'fence':
        win("When you land on the other side of the fence you realize youve landed in a familiar yard,your friends yard, your safe for now.")
    else:
        print("Invalid choice. Try again.")
        neighbors_yard()


def die(reason):
    print("\nGAME OVER: " + reason)
    play_again()


def win(reason):
    print("\nYou Win: " + reason)
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == 'yes':
        intro()
    else:
        print("Thanks for playing! Goodbye. ")

intro()
        

