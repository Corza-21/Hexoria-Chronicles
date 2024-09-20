yes=["yes", "okay", "ok", "sure", "yeah",  "yep", "ye", "yh", "yea", "ya", "y", "yup", "uhuh", "mhm", "mhmm", "mmm", "mm", "m", "yeh", "alright", "k", "all right", "of course", "duh", "why not"]
import string
import random
from Areas.alien_shop import AlienShop
from Areas.extra_molten import ExtraMoltenArea
from Areas.molten import MoltenArea
from Areas.rocky import RockyArea
from Areas.volcano import Volcano
from Areas.wasteland import Wasteland
from Game.player import Player
from Game.state import GameState

def main():
    player = Player()
    game_state = GameState(player)

    wasteland = Wasteland(game_state)
    rocky_area = RockyArea(game_state)
    molten_area = MoltenArea(game_state)
    extra_molten_area = ExtraMoltenArea(game_state)
    volcano = Volcano(game_state)
    alien_shop = AlienShop(game_state)

    # Connecting the areas
    wasteland.connect("north", molten_area)
    wasteland.connect("east", alien_shop)
    wasteland.connect("south", rocky_area)
    #wasteland.connect("west", forest)
    
    alien_shop.connect("west", wasteland)

    rocky_area.connect("north", wasteland)

    molten_area.connect("north", extra_molten_area)
    molten_area.connect("south", wasteland)

    extra_molten_area.connect("north", volcano)
    extra_molten_area.connect("south", molten_area)

    volcano.connect("south", extra_molten_area)

    start = True
    if start == True:
        print ("Welcome to Hexoria Chronicles. Please enjoy yourself.")
        game_state.player_name=input("Now, brave traveler, what is your superior name? ")
        print(f"Lovely to meet you, {game_state.player_name}")
        print("This will be a game about trying to survive in a world which is trying to end you all around.")
        ready=False
        while ready==False:
            are_you_ready=input("So, are you ready? ")
            are_you_ready=are_you_ready.lower()
            if are_you_ready in yes:
                ready=True
            else:
                print("Oh. Tell me when you're ready then.")
        warning_message=("Everything in this place is strange. Be careful on your journey brave traveller. You must keep yourself alive at all costs. Read fast, my messages are warnings, just as much as they are descriptions for you. If you see CAPITAL LETTERS, you should start worrying.")
        print(warning_message)
    else:
        pass

    player.current_area = wasteland
    player.current_area.enter(player)

if __name__ == "__main__":
    main()