from adventurelib import * 

bag = list()

say("You are in a lost world. Find a portal to escape!")

hill = Room("You are on a grey and black hill.")
hill.look = "You see a little house."

house = Room("You are at the front door of a house. There is an old lady. She asks for your name.")
house.look = "There is an old lady. She asks for your name."

current_room = hill

say(current_room)

@when('look')
def look():
    say(current_room.look)

@when('walk')
def walk():
    say("you get tired and stop")

@when('walk to ROOM')
def walk(room):
    room = {
        "hill": hill,
        "house": house
    }.get(room)
    global current_room
    if room:
        current_room = room
    say(current_room)

@when("take THING")
def take(thing):
    bag.append(thing)
    say(f"You take the {thing}. You now have a {', '.join(bag)} in your bag.")

start()