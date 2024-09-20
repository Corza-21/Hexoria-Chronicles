from area import Area

class RockyArea(Area):
    def __init__(self, game_state):
        description = (
            "This is quite a rocky area, you see small rocks around you, but there is no shimmering rock anymore. "
            "To your north you see a wasteland, it's where you began. "
            "To your east, you can see the entrance of a cave bulging out of the ground. "
            "To your south, you see what appears to be a large mansion. "
            "To your west, you see a plain barren area."
        )
        super().__init__("Rocky Area", description)
        self.rock_picked_up = False
        self.rock_in_hole = False

    def interact(self, player):
        while True:
            action = input("What do you do? ").lower()
            if action in ["north", "n", "go north", "walk north", "run north", "up"]:
                self.move(player, "north")
                break
            elif action in ["south", "s", "go south", "walk south", "run south", "down"]:
                self.move(player, "south")
                break
            elif action in ["east", "e", "go east", "walk east", "run east", "right"]:
                if self.rock_in_hole:
                    self.move(player, "east")
                    break
                else:
                    print("You have come to the entrance of the cave. You get the feeling you need to put something in the hole on the wall as an offering.")
                    sub_action = input("What do you do? ").lower()
                    if sub_action in ["put rock in hole", "put rock", "place rock", "insert rock", "put the rock in the hole"]:
                        self.rock_in_hole = True
                        print("Amazing, you put the rock in the hole. Fantastic problem-solving skills, traveller. You shall now enter the cave.")
                        self.move(player, "east")
                        break
                    else:
                        print("Sorry, I don't understand that. Let's go back to the rocky area.")
            elif action in ["west", "w", "go west", "walk west", "run west", "left"]:
                self.move(player, "west")
                break
            elif action in ["look", "look around", "see", "search", "find", "observe"]:
                print(self.description)
            elif action in ["sleep", "go to sleep", "doze off", "zzz"]:
                print("You slept.")
            elif action in ["score", "show score", "what is my score", "what's my score", "tell me my score"]:
                self.game_state.show_score()
            elif action in ["pick up rock", "pick up shimmering rock", "pick up shiny rock"]:
                if not self.rock_picked_up:
                    print("You picked up the shimmering rock. You feel that it could be useful somewhere.")
                    player.add_item("shimmering rock")
                    self.rock_picked_up = True
                else:
                    print("You already picked up the rock, you daft traveller!")
            else:
                print("Sorry, I don't understand that.")