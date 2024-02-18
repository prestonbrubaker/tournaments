import random
import matplotlib.pyplot as plt
import numpy as np

data = []


num_points = 100000000
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

#plt.hist(losers, bins=bin_C, density=True)
#plt.show()

def generate_pdf(data, bins=bin_C):
    hist, bin_edges = np.histogram(data, bins=bins)
    # Manually normalize the histogram to make the area under the histogram equal to 1
    hist = hist / np.sum(hist) / (bin_edges[1] - bin_edges[0])
    return hist

# Re-define calculate_shannon_entropy function to use histogram directly
def calculate_shannon_entropy(hist):
    probabilities = np.where(hist > 0, hist, np.finfo(float).eps)
    shannon_entropy = -np.sum(probabilities * np.log2(probabilities) * (1 / len(hist)))
    return shannon_entropy


# Generate the PDF (as a histogram) from the 'losers' data
hist = generate_pdf(winners, bins=bin_C)

# The expectation value function also needs to be adjusted to work directly with the histogram.
# Since the original function is expecting bin midpoints and probabilities, let's adjust it accordingly.
def calculate_expectation_value(hist, data_range=(0, 1)):
    bins = len(hist)
    bin_edges = np.linspace(data_range[0], data_range[1], bins+1)
    bin_midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2
    dx = (data_range[1] - data_range[0]) / bins  # Correctly calculating the bin width
    expectation_value = np.sum(bin_midpoints * hist * dx)
    return expectation_value

# Calculate expectation value and Shannon entropy again with the adjusted functions
expectation_value = calculate_expectation_value(hist)
shannon_entropy = calculate_shannon_entropy(hist)

print("Expectation Value: " + str(expectation_value))
print("Shannon Entropy: " + str(shannon_entropy) + " Bits")
