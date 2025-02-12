# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
'''
In pandas, a value's proportion in a categorical DataFrame column can be quickly calculated using the syntax:

prop = (df['col'] == val).mean()
'''
late_prop_samp = (late_shipments['late']=="Yes").mean()

# Print the results
print(late_prop_samp)
