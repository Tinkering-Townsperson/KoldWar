"""
This program is licensed under the GNU Affero General Public License to AfterNoon PM and all contributors.
"""

import adventurelib as adv
import os

adv.Room.add_direction('up', 'down')
ussr_bunker = adv.Room(
	"""
You are in the nuclear bunker. The walls are made of drab \033[0;30;47mwhite\033[1;37;40m concrete.
Hanging on the east wall are flags of the \033[0;33;41mcommunist\033[0;37;40m states of the world, forever comrades to The USSR.
On the north wall there is a ladder leading to a trapdoor with a one-way window.
"""
)

surface_ussr_bunker = adv.Room(
	"""
You are on the surface. beneath you lies the nuclear bunker.
"""
)

ussr_bunker.up = surface_ussr_bunker
ussr_bunker.contents = adv.Bag()
surface_ussr_bunker.contents = adv.Bag()
ussr_bunker.locked = dict()
surface_ussr_bunker.locked = dict()
current_room = ussr_bunker
inventory = adv.Bag()

rooms = [ussr_bunker, surface_ussr_bunker]

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
	global current_room
	next_room = current_room.exit(direction)
	if next_room:
		if direction in current_room.locked and current_room.locked[direction]:
			print(f"You can't go {direction} --- the door is locked.")
		else:
			current_room = next_room
			print(f"You go {direction}.")
			look()

	else:
		print(f"You can't go {direction}.")

@adv.when("look")
def look():
	adv.say(current_room)
	for item in current_room.contents:
		print(f"There is {item} here.")
	print(f"The following exits are present: {current_room.exits()}")

@adv.when("look at ITEM")
@adv.when("inspect ITEM")
def look_at(item: str):
	obj = inventory.find(item)
	if not obj:
		print(f"You don't have {item}.")
	else:
		print(f"It's an {obj}.")

@adv.when("take ITEM")
@adv.when("get ITEM")
@adv.when("pickup ITEM")
@adv.when("pick ITEM up")

def get(item: str):
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
	obj = inventory.take(item)
	if not obj:
		print(f"You don't have {item}")
	else:
		obj.use_item(current_room)


@adv.when("teleport PLACE")
@adv.when("tp PLACE")

def tp(place: str):
	print(place)
	
@adv.when("save")

def save():
	print(shelf)

if __name__=="__main__":
	look()
	adv.start()
