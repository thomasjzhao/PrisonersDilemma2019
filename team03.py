team_name = 'Copy Kitten'
strategy_name = 'Copycat'
strategy_description = 'Start with collude, then do whatever the other person did in the last round, meow.'


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    # collude on the first move:
    if len(my_history) == 0:
      return 'c'
    elif their_history[-1] == 'c':
      return 'c'
    elif their_history[-1] == 'b':
      return 'b'
