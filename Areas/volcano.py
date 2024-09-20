from area import Area

class Volcano(Area):
    def __init__(self, game_state):
        description = (
            "Well, you're smart, aren't you? Even with your excellent molten boots, the volcano swallowed you up like you were nothing."
        )
        super().__init__("Volcano", description)

    def interact(self, player):
        super().interact(player)