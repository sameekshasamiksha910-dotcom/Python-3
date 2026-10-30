# Remove blank lines from a text file

with open("input.txt", "r") as f:
    lines = f.readlines()

with open("output.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)

print("Blank lines removed successfully!")




#Employee salary analysis

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("employee.csv")

# Display employee details
print("Employee Details:")
print(df)

# Calculate salary statistics
print("\nAverage Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())

# Plot employee salaries
plt.bar(df["Name"], df["Salary"])
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Salary Analysis")
plt.show()