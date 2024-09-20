from area import Area
from data import GameData

class AlienShop(Area):
    def __init__(self, game_state):
        self.game_state = game_state
        self.shop_items = {
            "axe": 2,
            "ghost_zapper": 2,
            "basic_hint": 1,
            "good_hint": 3,
            "amazing_hint": 5,
            "pickaxe": 0,
        }
        self.shop_inventory = ["axe", "ghost_zapper", "basic_hint", "good_hint", "amazing_hint", "pickaxe"]
        if self.game_state.first_shop_visit:
            description = ("You have found your way into a strange shop which has all sorts of foreign items placed everywhere. You see an alien shopkeeper standing at the front desk, he looks distracted, but as if he could manage a conversation. Perhaps, you should talk to him. The only way out of this unique shop is West.")
            self.game_state.first_shop_visit = False
        else:
            description = ("Welcome back to Caitan's foreign shop for travellers and backpackers! The exit is West!")
        super().__init__("Alien Shop", description)

    def interact(self, player):
        flag = True
        while flag:
            action = input("Should you say hi? ").lower()
            if action in GameData.yes:
                print("You walk up to the alien who seems lost in thought. You gesture to him, but he doesn't seem to notice you. You make a louder noise. Finally, the alien turns and looks at you. He begins speaking as if scripted, ")
                action=input("“Welcome to Caitan's foreign shop for travellers and backpackers. Here you will find the greatest selection of foreign goods that you have never seen before. Of course, there will be a fee required. Would you like to be updated on our range?” ")
                flag = False
            else:
                print("In that case, it's time to leave before we get kicked out. ✨")
                flag = False
                self.move(player, "west")
        
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