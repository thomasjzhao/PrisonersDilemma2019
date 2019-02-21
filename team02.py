import random

team_name = 'fantasies(team2)'
team_strategy =  'Tit-For-Tat'
strategy_description = 'My first move, if i start first, is to collude. Then I will copy their moves, however if they betray, there is a 10% chance that I will forgive and collude.'

def move(my_history, their_history, my_score, their_score):
  while len(my_history) == 0:
    return 'c'
  if their_history[-1] == 'b':
    list1= ('b','c', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b')
    return random.choice(list1)
  elif their_history[-1] == 'c':
    return 'c'
