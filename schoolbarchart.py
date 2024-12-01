import matplotlib.pyplot as plt

# Data: School results over five consecutive years
years = ['2019', '2020', '2021', '2022', '2023']
results = [85, 90, 88, 92, 95]

# Plotting the bar chart
plt.bar(years, results, color='orange')

# Adding title and labels
plt.title("School Results Over 5 Consecutive Years")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")

# Displaying the bar chart
plt.show()
