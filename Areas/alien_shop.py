from area import Area

class AlienShop(Area):
    def __init__(self, game_state):
        self.game_state = game_state
        self.first_visit = True
        self.shop_items = {
            "axe": 2,
            "ghost_zapper": 2,
            "basic_hint": 1,
            "good_hint": 3,
            "amazing_hint": 5,
            "pickaxe": 0,
        }
        self.shop_inventory = ["axe", "ghost_zapper", "basic_hint", "good_hint", "amazing_hint", "pickaxe"]
        description = "You have found your way into a strange shop..."
        super().__init__("Alien Shop", description)

    def interact(self, player):
        if self.first_visit:
            print("Welcome to Caitan's foreign shop for travellers and backpackers!")
            self.first_visit = False
        else:
            print("Welcome back to Caitan's foreign shop!")
        
        action = input("What would you like to do? ").lower()
        # Buying an Axe
        if action in ["buy axe", "get axe"] and "axe" in self.shop_inventory:
            if self.game_state.emeralds >= self.shop_items["axe"]:
                player.add_item("axe")
                self.shop_inventory.remove("axe")
                self.game_state.emeralds -= self.shop_items["axe"]
                print("You have purchased an axe.")
            elif "axe" not in self.shop_inventory:
                print("You've already bought that.")
            else:
                print("You don't have enough emeralds.")
        # Buying a Ghost Zapper
        elif action in ["buy ghost zapper", "get ghost zapper"] and "ghost_zapper" in self.shop_inventory:
            if self.game_state.emeralds >= self.shop_items["ghost_zapper"]:
                player.add_item("ghost zapper")
                self.shop_inventory.remove("ghost_zapper")
                self.game_state.emeralds -= self.shop_items["ghost_zapper"]
                print("You have purchased a ghost zapper.")
            elif "ghost_zapper" not in self.shop_inventory:
                print("You've already bought that.")
            else:
                print("You don't have enough emeralds.")
        # Buying a Basic Hint
        elif action in ["buy basic hint", "get basic hint"]:
            if self.game_state.emeralds >= self.shop_items["basic_hint"] and "basic_hint" in self.shop_inventory:
                player.add_item("basic hint")
                self.shop_inventory.remove("basic_hint")
                self.game_state.emeralds -= self.shop_items["basic_hint"]
                print("You have purchased a basic hint.")
            elif "basic_hint" not in self.shop_inventory:
                print("You've already bought that.")
            else:
                print("You don't have enough emeralds.")
        # Buying a Good Hint
        elif action in ["buy good hint", "get good hint"] and "good_hint" in self.shop_inventory:
            if self.game_state.emeralds >= self.shop_items["good_hint"]:
                player.add_item("good hint")
                self.shop_inventory.remove("good_hint")
                self.game_state.emeralds -= self.shop_items["good_hint"]
                print("You have purchased a good hint.")
            else:
                print("You don't have enough emeralds.")
        # Buying an Amazing Hint
        elif action in ["buy amazing hint", "get amazing hint"] and "amazing_hint" in self.shop_inventory:
            if self.game_state.emeralds >= self.shop_items["amazing_hint"]:
                player.add_item("amazing hint")
                self.shop_inventory.remove("amazing_hint")
                self.game_state.emeralds -= self.shop_items["amazing_hint"]
                print("You have purchased an amazing hint.")
        #Buying a Pickaxe
        elif action in ["buy pickaxe", "get pickaxe"] and "pickaxe" in self.shop_inventory:
            if "pickaxe" in self.shop_inventory:
                player.add_item("pickaxe")
                self.shop_inventory.remove("pickaxe")
            else:
                print("You've already bought that.")
        else:
            print("Sorry, I don't understand that.")