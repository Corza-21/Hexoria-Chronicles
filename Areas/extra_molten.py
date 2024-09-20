from area import Area

class ExtraMoltenArea(Area):
    def __init__(self, game_state):
        self.game_state = game_state
        if "boots" in self.game_state.player.player_inventory:
            description = (
                "Your fancy special boots allow you to walk comfortably into a BEAUTIFUL new area. "
                "This area is even more molten than the last. All around you see gorgeous emerald ores. "
                "To your west lays a molten area showing signs of valuable emerald ore."
            )
        else:
            description = f"You have walked onto the molten rock without any special boots to save yourself from a tragic death. Sadly, you have died, {self.game_state.player.player_name}. Better luck next time."
        super().__init__("Extra Molten Area", description)

    def interact(self, player):
        super().interact(player)
        if "pickaxe" in self.game_state.player.player_inventory:
            if not other_ores_mined:
                print("Excellent, you have mined the seven ores you see in front of you.")
                self.game_state.emeralds += 7
                other_ores_mined = True
            else:
                print("There are no more emerald ores, sorry.")
        else:
            print("You need a pickaxe to mine ore.")