#Calculating p-values
#to determine whether to choose the null hypothesis or the alternative hypothesis, you need to calculate a p-value from the z-score.

#The null hypothesis, is that the proportion of late shipments is six percent.
#alternative hypothesis, is that the proportion of late shipments is greater than six percent.
# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Calculate the p-value
p_value = 1 - norm.cdf(z_score)
                 
# Print the p-value
print(p_value)
