# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product

probs = counts / amir_deals.shape[0]

#counts / counts.sum()
print(probs)
"""
     Unnamed: 0    product   client status   amount  num_users
0             1  Product F  Current    Won  7389.52         19
1             2  Product C      New    Won  4493.01         43
2             3  Product B      New    Won  5738.09         87
3             4  Product I  Current    Won  2591.24         83
4             5  Product E  Current    Won  6622.97         17
..          ...        ...      ...    ...      ...        ...
173         174  Product A  Current   Lost  5835.32         23
174         175  Product D  Current    Won  6377.50         12
175         176  Product D  Current    Won  3537.61         28
176         177  Product A  Current    Won  6448.07         34
177         178  Product D      New   Lost  7320.05         72


"""
