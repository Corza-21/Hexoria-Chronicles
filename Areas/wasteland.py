from area import Area

class Wasteland(Area):
    def __init__(self, game_state):
        description = (
            "This is a wasteland, you can see tumbleweeds floating by. "
            "To your north, you see some red, orange, and yellow, but you can't make out what it is from here. "
            "To your east, you see what looks to be some kind of building. "
            "It is small and homely with the door wide open to visitors. "
            "To your south, you see a very rocky area. "
            "To your west you see some trees, it must be a forest."
        )
        super().__init__("Wasteland", description)