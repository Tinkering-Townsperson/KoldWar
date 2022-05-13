"""
This program is licensed under the GNU Affero General Public License to AfterNoon PM and all contributors.
"""

import adventurelib as adv
import os

adv.Room.add_direction('up', 'down')
bunker = adv.Room(
	"""
You are in the nuclear bunker. The walls are made of drab \033[0;30;47mwhite\033[1;37;40m concrete.
Hanging on the east wall are flags of the communist states of the world, forever comrades to The USSR.
On the north wall there is a ladder leading to a trapdoor with a one-way window.
"""
)

surface_bunker = adv.Room(
	"""

"""
)

bunker.up = surface_bunker
bunker.contents = adv.Bag()
surface_bunker.contents = adv.Bag()
bunker.locked = dict()
surface_bunker.locked = dict()
current_room = bunker
inventory = adv.Bag()

# Define your movement commands
@adv.when("go DIRECTION")
@adv.when("north", direction="north")
@adv.when("south", direction="south")
@adv.when("east", direction="east")
@adv.when("west", direction="west")
@adv.when("up", direction="up")
@adv.when("down", direction="down")
@adv.when("n", direction="north")
@adv.when("s", direction="south")
@adv.when("e", direction="east")
@adv.when("w", direction="west")
@adv.when("u", direction="up")
@adv.when("d", direction="down")

def go(direction: str):
    """Processes your moving direction

    Arguments:
        direction {str} -- which direction does the player want to move
    """

    # What is your current room?
    global current_room

    # Is there an exit in that direction?
    next_room = current_room.exit(direction)
    if next_room:
        # Is the door locked?
        if direction in current_room.locked and current_room.locked[direction]:
            print(f"You can't go {direction} --- the door is locked.")
        else:
            current_room = next_room
            print(f"You go {direction}.")
            look()

    # No exit that way
    else:
        print(f"You can't go {direction}.")

# How do you look at the room?
@adv.when("look")
def look():
    """Looks at the current room"""

    # Describe the room
    adv.say(current_room)

    # List the contents
    for item in current_room.contents:
        print(f"There is {item} here.")

    # List the exits
    print(f"The following exits are present: {current_room.exits()}")

# How do you look at items?
@adv.when("look at ITEM")
@adv.when("inspect ITEM")
def look_at(item: str):

    # Check if the item is in your inventory or not
    obj = inventory.find(item)
    if not obj:
        print(f"You don't have {item}.")
    else:
        print(f"It's an {obj}.")

# How do you pick up items?
@adv.when("take ITEM")
@adv.when("get ITEM")
@adv.when("pickup ITEM")
def get(item: str):
    """Get the item if it exists

    Arguments:
        item {str} -- The name of the item to get
    """
    global current_room

    obj = current_room.contents.take(item)
    if not obj:
        print(f"There is no {item} here.")
    else:
        print(f"You now have {item}.")
        inventory.add(obj)

# How do you use an item?
@adv.when("unlock door", item="key")
@adv.when("use ITEM")
def use(item: str):
    """Use an item, consumes it if used

    Arguments:
        item {str} -- Which item to use
    """

    # First, do you have the item?
    obj = inventory.take(item)
    if not obj:
        print(f"You don't have {item}")

    # Try to use the item
    else:
        obj.use_item(current_room)

if __name__=="__main__":
	look()

	adv.start()
