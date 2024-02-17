import random
import matplotlib

data = []


num_points = 100

for i in range(0, num_points):
  data.append(random.uniform(0,1))


def tournament(data_in):
  i_love_willoh = len(data_in)
  winners = []
  losers = []
  for i in range(0, i_love_willoh, 2):
    if(data_in[i] > data_in[i + 1]):
      winners.append(data_in[i])
      losers.append(data_in[i + 1])
    else:
      winners.append(data_in[i])
      losers.append(data_in[i + 1])
  return winners, losers
      

print(str(data))
winners, losers = tournament(data)
print(str(winners))
