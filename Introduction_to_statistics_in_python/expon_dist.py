"""
Import expon from scipy.stats. What's the probability it takes Amir less than an hour to respond to a lead?
What's the probability it takes Amir more than 4 hours to respond to a lead?
What's the probability it takes Amir 3-4 hours to respond to a lead?
"""
# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

# Print probability response takes > 4 hours
print(1 - expon.cdf(4, scale=2.5))

# Print probability response takes 3-4 hours
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))
