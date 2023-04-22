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
          self.drawn.append(self.contents.pop(random.randrange(len(self.contents))))
        return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n_success = 0
    for i in range(num_experiments):
      hat_copy = copy.deepcopy(hat)
      drawn = hat_copy.draw(num_balls_drawn)
      correct_balls = 0
      for k,v in expected_balls.items():
        if drawn.count(k) >= v:
          correct_balls += 1      
      if correct_balls == len(expected_balls):
        n_success += 1 
    return n_success / num_experiments
