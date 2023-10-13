import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Numpy
# a. Create an array with shape (4, 3) of:
# all zeros
zeros_array = np.zeros((4, 3))
# ones
ones_array = np.ones((4, 3))
# numbers from 0 to 11
numbers_array = np.arange(12).reshape((4, 3))

print("An array of zeros:")
print(zeros_array)
print("\nAn array with ones:")
print(ones_array)
print("\nAn array of numbers from 0 to 11:")
print(numbers_array)

# b. Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1
x_values = np.arange(1, 101, 1)
F_x = 2 * x_values**2 + 5

table_b = np.column_stack((x_values, F_x))
print("\nb. Tabulated function F(x) = 2x^2 + 5:")
print(table_b)

# c. Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1
x_values = np.arange(-10, 11, 1)
F_x = np.exp(-x_values)

table_c = np.column_stack((x_values, F_x))
print("\nc. Tabulated function F(x) = e^(-x):")
print(table_c)


# 2. Pandas

# а. Import the dataset (тільки так запрацювало, з повним шляхом)

df = pd.read_csv("euro2012.csv")
print(df.head())

# b. Select only the Team, Yellow Cards and Red Cards columns.

selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print(selected_columns)

# c. How many teams participated in the Euro2012?
num_teams = df['Team'].nunique()
print(f"The number of teams that took part in Euro-2012: {num_teams}")

# d. Filter teams that scored more than 6 goals
high_scorers = df[df['Goals'] > 6]
print("Teams that scored more than 6 goals:")
print(high_scorers)

# 3. DataViz

tips = sns.load_dataset("tips")
print(tips.head())

# Strip Plot
sns.stripplot(x="day", y="total_bill", data=tips)
plt.show()

# Box Plot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# Violin Plot
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()

# Bar Plot
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()

# Count Plot
sns.countplot(x="day", data=tips)
plt.show()

# Joint Plot
sns.jointplot(x="total_bill", y="tip", data=tips)
plt.show()

# Pair Plot
sns.pairplot(tips)
plt.show()
