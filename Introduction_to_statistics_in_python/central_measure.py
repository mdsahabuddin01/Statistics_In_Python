# Import numpy with alias np
import numpy as np

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption["country"] == "USA"]

# Calculate mean consumption in USA
print(np.mean(usa_consumption["consumption"]))

# Calculate median consumption in USA
print(np.median(usa_consumption["consumption"]))

# Subset food_consumption to get the rows where food_category is 'rice'.
# Create a histogram of co2_emission in rice_consumption DataFrame and show the plot.
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption["food_category"] == "rice"]

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption["co2_emission"])
plt.show()

#
# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption["co2_emission"].agg([np.mean, np.median]))

