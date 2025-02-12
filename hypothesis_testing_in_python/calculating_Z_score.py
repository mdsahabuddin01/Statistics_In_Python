'''

Standardization: We need to make sure our numbers are on the same scale so that our results are meaningful, no matter the units (like Euros or US dollars).

Z-Score: This is a special number we calculate to help us understand how far our sample result is from what we expect. It helps us in hypothesis testing.

To Calculate a Z-Score: You need:

Sample Statistic: The actual result from your data, called late_prop_samp.
Hypothesized Statistic: What you expect the result to be.
Standard Error: A measure of how much your sample result might vary, estimated from late_shipments_boot_distn.

'''

# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06
#Calculate the standard error from the standard deviation of the bootstrap distribution.
# Calculate the standard error
std_error = np.std(late_shipments_boot_distn)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Print z_score
print(z_score)
#the z-score helps you understand if the percentage of late shipments you observed is typical or if it's very different from what you expected (6%). A high or low z-score means your sample is far from the expected proportion.
