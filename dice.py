import random

class Dice:
  def roll(self):
    return random.randrange(1, 6)
  
  # def roll_multiple_dice(self, count):
  #   result = []
  #   for i in range(0, count):
  #     result.appenf(self.roll)