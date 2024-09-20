from area import Area

class MoltenArea(Area):
    def __init__(self, game_state):
        self.game_state = game_state
        if "boots" in self.game_state.player.player_inventory:
            if self.game_state.two_ores_mined != True:
                minor_description="Directly in front of you, you can see 2 shimmering green ores, they must be emerald ores. "
            else:
                minor_description=""
            description_molten_area=f"Your stylish molten boots allow you to walk on the molten rock with ease. {minor_description}Beyond that, you can see what looks to be six of the gorgeous emerald ores. They look like they are longing to be mined. To your north, you see what looks to be a volcano that is dangerously close to erupting. To your west, you see what looks to be more emerald ores than you could ever imagine. To your south, you can see a wasteland. You just see fog to the west, it must be a wall."
            #print(description_molten_area)
        else:
            if self.game_state.two_ores_mined != True:
                minor_description="The good news is you see some rocks which appear to be shimmering with a distinct green colour. It must be some kind of ore. Mining that ore could be invaluable. "
            else:
                minor_description=""
            description_molten_area=f"You have stepped onto a molten rock area. If you step any further north, you will very frighteningly melt into the molten rock, gone forever. {minor_description}You are unable to see what is North, East, or West because going any further forward would ensure your death. To your south, you of course see a wasteland."
            #print(description_molten_area)
        super().__init__("Molten Area", description_molten_area)

    def interact(self, player):
        super().interact(player)
        if "pickaxe" in self.game_state.player.player_inventory:
            if not self.game_state.two_ores_mined:
                print("Excellent, traveller, you have mined the two ores.")
                self.game_state.emeralds += 2
                self.game_state.two_ores_mined = True
            elif not self.game_state.six_ores_mined:
                print("Amazing, traveller, you mined the six ores.")
                self.game_state.emeralds += 6
                self.game_state.six_ores_mined = True
        else:
            print("You need a pickaxe to mine ore.")