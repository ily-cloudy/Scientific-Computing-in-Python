import random
# note 1: 'import copy' would be (slightly?) more effective but i, for some reason, decided to remove it during troubleshooting. Make sure to use copy.deepcopy! See line 25-27.   

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

# mess warning! proceed at your own risk. 
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n_success = 0
    for i in range(num_experiments):
        success = True
        # creating copies for each list, as both the draw method and the for-loop, which checks the if the draw was succesful, will remove elements from lists.  
        expected_copy = expected_balls.copy()
        hat_copy = Hat()
        hat_copy.contents = hat.contents.copy()
        drawn = hat_copy.draw(num_balls_drawn)
        # this can probably be simplified, though all my attempts (1) failed horrendously.
        for j in drawn:
            if j in expected_copy:
                expected_copy[j] -= 1
                if expected_copy[j] == 0:
                    del expected_copy[j]
                    if len(expected_copy) == 0:
                        break
            else:
                success = False
                break
        # success counter
        if success:
            n_success += 1
    # returns probability
    return n_success / num_experiments

# test run c:
hat = Hat(black=6, red=4, green=3)

print(experiment(hat=hat,
                 expected_balls={"red":2,"green":1},
                 num_balls_drawn=5,
                 num_experiments=2000)
)
