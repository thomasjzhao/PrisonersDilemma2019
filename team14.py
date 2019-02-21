team_name = '1 IQ man'
strategy_name = 'B niCe'
strategy_description = 'If they betray then we betray, if not, then we collude'



def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'c'
  elif len(my_history) > 0:
    if my_score < their_score: 
      if (their_history[-1]) == 'b':
        return 'b'
      else:
        return 'c'  
    if my_score > their_score:
      return 'b'

