import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = [ball for ball in balls for i in range(balls[ball])]

    def draw(self, draw_number):
        draw_list = []
        if draw_number >= len(self.contents):
            return self.contents
        for i in range(draw_number):
            choice = random.choice(self.contents)
            self.contents.remove(choice)
            draw_list.append(choice)
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_list = []

    for key, value in expected_balls.items():
        for x in range(value):
            expected_list += key.split()
    m = 0
    for n in range(num_experiments):
        trial = copy.deepcopy(hat)
        draw = trial.draw(num_balls_drawn)
        result = list((Counter(expected_list) - Counter(draw)).elements())
        if not result:
            m += 1
    probability = m / num_experiments
    return probability
