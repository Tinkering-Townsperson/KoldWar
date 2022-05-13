"""
This program is licensed under the GNU Affero General Public License to AfterNoon PM and all contributors.
"""

import adventurelib as adv
import os

bunker = adv.Room(
	"""
You are in the nuclear bunker. The walls are made of drab white concrete.
Hanging on the east wall are flags of the communist states of the world, forever comrades to The USSR.
On the north wall there is a ladder leading to a trapdoor with a one-way window.
"""
)

surface_bunker = adv.Room(
	"""

"""
)

bunker.up = surface_bunker

current_room = bunker

if __name__=="__main__":
	look()
	
	adv.start()
