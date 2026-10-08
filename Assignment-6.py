profit = [25, 24, 15]
weight = [18, 15, 10]
capacity = 20

n = len(profit)

# Calculate profit/weight ratio
ratio = [profit[i] / weight[i] for i in range(n)]

# Sort items by ratio (highest first)
order = sorted(range(n), key=lambda i: ratio[i], reverse=True)

total_profit = 0

for i in order:
    if capacity <= 0:
        break

    if weight[i] <= capacity:
        capacity -= weight[i]
        total_profit += profit[i]
    else:
        fraction = capacity / weight[i]
        total_profit += profit[i] * fraction
        capacity = 0

print("Maximum Profit:", total_profit)