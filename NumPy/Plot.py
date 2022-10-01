# Find cumulative monthly sales for each industry
cumulative_monthly_industry_sales = monthly_sales.cumsum(axis=0)
print(cumulative_monthly_industry_sales)

# Plot each industry's cumulative sales by month as separate lines
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 0], label="Liquor Stores")
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 1], label="Restaurants")
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 2], label="Department stores")
plt.legend()
plt.show()

   [[  4134  23925   8657]
     [  8250  47800  17799]
     [ 12923  74997  28444]
     [ 17503 100634  38900]
     [ 22612 128629  50199]
     [ 27623 156048  60824]
     [ 32868 183353  71454]
     [ 38138 211113  83004]
     [ 42818 236101  92766]
     [ 47731 261903 103222]
     [ 53043 287308 116623]
     [ 59673 315105 135026]]