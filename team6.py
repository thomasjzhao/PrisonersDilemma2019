####
#     Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Do not trust us'
team_strategy =  'If they have a positive score we betray them. If they have zero we collude. If it is less then zero we will always collude. Unless they have just betrayed.'
strategy_description = 'Math is the univarsal language.'
    


def move(my_history, their_history, my_score, their_score):
    # collude if their score 0
    if int(their_score) == 0:
      return 'c'
    # If they have a positive score betray
    elif int(their_score) > 0:
      return 'b'
    # If they have a negitive score collude unless they have just betrayed
    elif int(their_score) < 0:
      if len(my_history) >= 1 and their_history[-1] == 'b':
        return 'b'
      else:
        return 'c'
