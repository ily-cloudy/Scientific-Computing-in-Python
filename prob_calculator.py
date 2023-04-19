import random
import copy

class Hat:
    def __init__(self, **entries):
        self.contents = []
        for k, v in entries.items():
            for i in range(v):
                self.contents.append(k)   
    
    def draw(self, n):
        self.drawn = []
        if n > len(self.contents):
            n = len(self.contents)
        for i in range(n):
            ball = random.choice(self.contents)
            self.drawn.append(ball)
            self.contents.remove(ball)
        return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    n_success = 0
    n_total = 0
    for k, v in expected_balls.items():
        for i in range(v):
            expected.append(k)
    for i in range(num_experiments):
        drawn = copy.deepcopy(hat).draw(num_balls_drawn)
        if all(i in drawn for i in expected):
            n_success += 1 
            n_total += 1
        else:
            n_total += 1 
    probability = n_success / n_total
    return probability