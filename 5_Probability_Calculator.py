import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for colour, count in kwargs.items():
            self.contents += [colour] * count
    
    def draw(self, n):
        if n > len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
        else:
            drawn = random.sample(self.contents, n)
            for ball in drawn:
                self.contents.remove(ball)

        return drawn
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        is_success = True

        for colour, count in expected_balls.items():
            if drawn_balls.count(colour) < count:
                is_success = False
                break
                
        if is_success:
            success_count += 1

    return success_count / num_experiments
            
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print("Probability:", probability)