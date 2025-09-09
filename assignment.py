# assignment.py
# Objective:
# Load and analyze a dataset using pandas
# Create simple plots with matplotlib & seaborn for visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# ----------------------------
# Task 1: Load and Explore Data
# ----------------------------
try:
    # Load the Iris dataset as a pandas DataFrame
    iris = load_iris(as_frame=True)
    df = iris.frame

    print("✅ Dataset loaded successfully!\n")

    # Display first 5 rows
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")

    # Check data types
    print("Dataset info:")
    print(df.info(), "\n")

    # Check missing values
    print("Missing values in each column:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (Iris has no missing values; showing example if needed)
    df = df.fillna(method='ffill')

except FileNotFoundError:
    print("❌ Dataset not found. Please check path.")
except Exception as e:
    print("❌ Error while loading dataset:", e)


# ----------------------------
# Task 2: Basic Data Analysis
# ----------------------------

# Basic statistics
print("Statistical Summary of Dataset:")
print(df.describe(), "\n")

# Grouping: Average petal length by species
grouped = df.groupby("target")["petal length (cm)"].mean()
print("Average Petal Length per Species (by target ID):")
print(grouped, "\n")

# Example finding
print("🌟 Observation: Species with target =", grouped.idxmax(), 
      "has the highest average petal length.\n")


# ----------------------------
# Task 3: Data Visualization
# ----------------------------

sns.set(style="whitegrid")

# 1. Line chart: Sepal length trend over samples
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["sepal width (cm)"], label="Sepal Width")
plt.title("Sepal Measurements Trend Over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Size (cm)")
plt.legend()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(6, 5))
sns.barplot(x="target", y="petal length (cm)", data=df, estimator="mean")
plt.title("Average Petal Length per Species")
plt.xlabel("Species (Target ID)")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram: Distribution of sepal length
plt.figure(figsize=(6, 5))
plt.hist(df["sepal length (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(7, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", 
                hue="target", data=df, palette="viridis")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
