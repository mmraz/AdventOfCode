#!/usr/bin/env python3

inputs = list()
DEBUG = False

with open('input', 'r') as f:
    inputs = f.read().splitlines()

balls = [int(ball) for ball in inputs.pop(0).split(',')]
if DEBUG:
    print(balls)
inputs.pop(0)

card = 0
cards = list()
cards.append(list())
while(len(inputs) > 0):
  line = inputs.pop(0)
  if len(line) == 0:
      if DEBUG:
        print(cards[card])
      card += 1
      cards.append(list())
      continue
  cards[card].extend([int(n) for n in line.split()])


def winner(card):
    for i in range(5):
      # row all stamped
      if card[(i*5):((i+1)*5)].count(-1) == 5:
        return True
      # column all stamped
      if [card[i+r] for r in range(0,25,5)].count(-1) == 5:
        return True
    return False

stamp_idx = 0
winner_cnt = 0
for ball in balls:
    for c in range(len(cards)):
        try:
            stamp_idx = cards[c].index(ball)
        except:
            continue
        cards[c].pop(stamp_idx)
        cards[c].insert(stamp_idx,-1)
        if winner(cards[c]):
          winner_cnt += 1
          card_total = sum(filter(lambda x: x != -1, cards[c]))
          if DEBUG:
            print(f"c {c} card_total {card_total} ball {ball}")
            print(f"called balls {balls[:balls.index(ball)]}")
            print(f"card {cards[c]}")
          cards[c].clear()
          if winner_cnt == len(cards):
            print(card_total * ball)
            exit()
