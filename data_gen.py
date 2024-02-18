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

plt.hist(losers, bins=bin_C, density=True)
plt.show()

def generate_pdf(data, bins=100):
    """
    Generates a discrete probability density function (PDF) from a list of data, only returning the histogram.

    :param data: List of data points.
    :param bins: Number of bins for the histogram.
    :return: Probability density for each bin.
    """
    hist, _ = np.histogram(data, bins=bins, density=True)
    return hist

# Re-define calculate_shannon_entropy function to use histogram directly
def calculate_shannon_entropy_in_bits(hist):
    """
    Calculates the Shannon entropy from a histogram in bits.

    :param hist: Histogram representing the probability density of each bin.
    :return: Shannon entropy in bits.
    """
    probabilities = np.where(hist > 0, hist, np.finfo(float).eps)
    shannon_entropy = -np.sum(probabilities * np.log2(probabilities) * (1 / len(hist)))
    return shannon_entropy


# Generate the PDF (as a histogram) from the 'losers' data
hist = generate_pdf(winners, bins=bin_C)

# The expectation value function also needs to be adjusted to work directly with the histogram.
# Since the original function is expecting bin midpoints and probabilities, let's adjust it accordingly.
def calculate_expectation_value(hist, data_range=(0, 1)):
    """
    Calculates the expectation value from a histogram, assuming a uniform distribution of bin midpoints.

    :param hist: Histogram representing the probability density of each bin.
    :param data_range: Tuple indicating the min and max values of the data range.
    :return: Expectation value.
    """
    bins = len(hist)
    bin_edges = np.linspace(data_range[0], data_range[1], bins+1)
    bin_midpoints = (bin_edges[:-1] + bin_edges[1:]) / 2
    dx = bin_midpoints[1] - bin_midpoints[0]  # Assuming evenly spaced bins
    expectation_value = np.sum(bin_midpoints * hist * dx)
    return expectation_value

# Calculate expectation value and Shannon entropy again with the adjusted functions
expectation_value = calculate_expectation_value(hist)
shannon_entropy = calculate_shannon_entropy(hist)

print("Expectation Value: " + str(expectation_value))
print("Shannon Entropy: " + str(shannon_entropy) + " Bits")
