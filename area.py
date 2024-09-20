class Area:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}

    def connect(self, direction, area):
        self.connections[direction] = area

    def enter(self, player):
        print(self.description)
        self.interact(player)

    def interact(self, player):
        while True:
            action = input("What do you do? ").lower()
            if action in ["north", "n", "go north", "walk north", "run north", "up"]:
                self.move(player, "north")
            elif action in ["south", "s", "go south", "walk south", "run south", "down"]:
                self.move(player, "south")
            elif action in ["east", "e", "go east", "walk east", "run east", "right"]:
                self.move(player, "east")
            elif action in ["west", "w", "go west", "walk west", "run west", "left"]:
                self.move(player, "west")
            elif action in ["look", "look around", "see", "search", "find", "observe"]:
                print(self.description)
            elif action in ["sleep", "go to sleep", "doze off", "zzz"]:
                print("You slept.")
            elif action in ["score", "show score", "what is my score", "what's my score", "tell me my score"]:
                self.game_state.show_score()
            elif action in ["mine", "mine ores"]:
                self.mine(player)
            else:
                print("Sorry, I don't understand that.")

    def move(self, player, direction):
        if direction in self.connections:
            player.current_area = self.connections[direction]
            player.current_area.enter(player)
        else:
            print("You can't go that way.")