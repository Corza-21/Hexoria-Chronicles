class GameState:
    def __init__(self, player):
        self.player = player
        self.emeralds = 0
        self.two_ores_mined = False
        self.six_ores_mined = False
        self.other_ores_mined = False

    def show_score(self):
        print(f"Emeralds: {self.emeralds}")