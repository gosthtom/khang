import random

class Game:
    def __init__(self):   
        self.scores = []

    def score(self):
        return random.randint(0, 100) 
    def quantity(self):
        return random.randint(1, 5) 

    def total_score(self):
        return sum(self.scores)

    def add_score(self, value):
        self.scores.append(value)

    def reset_scores(self):
        self.scores = []

    def play(self):
        print("Bắt đầu trò chơi!")
        num_rolls = self.quantity()
        print(f"Số lần gieo trong trò chơi này: {num_rolls}")
        for i in range(num_rolls):
            current_score = self.score()
            print(f"Lần gieo thứ {i+1}: {current_score} điểm")
            self.add_score(current_score)
        print(f"Tổng điểm của trò chơi: {self.total_score()}")
        print("Kết thúc trò chơi!")

if __name__ == "__main__":
    game = Game()
    game.play()