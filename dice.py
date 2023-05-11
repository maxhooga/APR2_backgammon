import random

class Dice:
  def roll(self):
    results = []
    results.append(random.randrange(1, 6))
    results.append(random.randrange(1, 6))
    if results[0] == results[1]:
      results.append(results[0])
      results.append(results[0])
    return results
  