class Player:
    def __init__(self):
        self.player_inventory = []
        self.current_area = None
        self.player_name = ""

    def add_item(self, item):
        self.player_inventory.append(item)