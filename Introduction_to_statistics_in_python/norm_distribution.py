"""
Instructions 4/4
25 XP
What's the probability of Amir closing a deal worth less than $7500?
What's the probability of Amir closing a deal worth more than $1000?
What's the probability of Amir closing a deal worth between $3000 and $7000?
What amount will 25% of Amir's sales be less than?"""
# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

print(prob_less_7500)

# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)

print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)

print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)

print(pct_25)
