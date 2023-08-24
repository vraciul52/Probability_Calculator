import random
# Consider using the modules imported above.

import copy


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      self.contents.extend([color] * count)

  def draw(self, num_balls):
    if num_balls >= len(self.contents):
      drawn_balls = self.contents
      self.contents = []
    else:
      drawn_indices = random.sample(range(len(self.contents)), num_balls)
      drawn_balls = [self.contents[i] for i in drawn_indices]
      self.contents = [
        ball for i, ball in enumerate(self.contents) if i not in drawn_indices
      ]
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_successful_experiments = 0

  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    success = True

    for color, count in expected_balls.items():
      if drawn_balls.count(color) < count:
        success = False
        break

    if success:
      num_successful_experiments += 1

  probability = num_successful_experiments / num_experiments

  return probability