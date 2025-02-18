#Variance and standard deviation

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby("food_category")["co2_emission"].agg([np.var, np.std]))

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption["food_category"] =="beef"]['co2_emission'].hist()
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption["food_category"] =="eggs"]['co2_emission'].hist()
plt.show()

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption["co2_emission"], [0, 0.25, 0.5, 0.75, 1]))


