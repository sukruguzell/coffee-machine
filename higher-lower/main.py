from art import logo
print(logo)
from game_data import data
flag=True
import random
from art import vs

score=0
while flag:
  rand=random.choice(data)
  rand2=random.choice(data)
  print(f"Compare A: {rand['name']} ,{rand['description']} ,{rand['country']} ")
  print(vs)
  print(f"Compare B: {rand2['name']} ,{rand2['description']} ,{rand2['country']} ")
  answer=input("Who has more followers?Type 'A' or 'Type B':")
  if answer=='A':
    if rand['follower_count']>rand2['follower_count']:
      print("You are right")
      print(f"A: {rand['follower_count']}  ")
      print(f"B: {rand2['follower_count']}  ")
      score +=1
      print(score)
    else:
      print("You are wrong")
      print(f"A: {rand['follower_count']}  ")
      print(f"B: {rand2['follower_count']}  ")
      flag=False
  if answer=='B':
    if rand['follower_count']<rand2['follower_count']:
      print("You are right")
      print(f"A: {rand['follower_count']}  ")
      print(f"B: {rand2['follower_count']}  ")
      score +=1
      print(score)
    else:
      print("You are wrong")
      print(f"A: {rand['follower_count']}  ")
      print(f"B: {rand2['follower_count']}  ")
      flag=False

print(f"Your score {score}")