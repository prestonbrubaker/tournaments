import random
import matplotlib.pyplot as plt

data = []


num_points = 1000000
bin_C = 100

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
      winners.append(data_in[i+1])
      losers.append(data_in[i])
  return winners, losers
      

#print(str(data))
winners, losers = tournament(data)
winners_w2l0, losers_w1l1 = tournament(winners)

winners_w3l0, losers_w2l1 = tournament(winners_w2l0)

plt.hist(winners_w3l0, bins=bin_C, density=True)
plt.show()
