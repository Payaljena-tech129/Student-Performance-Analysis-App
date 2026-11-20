import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("STUDENT PERFORMANCE ANALYSIS")

# Create dataset
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Riya"],
    "Maths": [85, 90, 45, 78, 95],
    "Science": [80, 95, 50, 85, 92],
    "English": [75, 88, 55, 80, 90]
}

df = pd.DataFrame(data)

print(df)

# Calculate total marks
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Calculate average marks
df["Average"] = df["Total"] / 3

print("\nStudent Performance:")
print(df)

# Find topper
topper = df.loc[df["Average"].idxmax()]

print("\nTopper:", topper["Name"])
print("Average Marks:", topper["Average"])

# Create Seaborn graph
plt.figure(figsize=(8, 5))

sns.barplot(x="Name", y="Average", data=df)

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("STUDENT PERFORMANCE ANALYSIS")

# Create dataset
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Riya"],
    "Maths": [85, 90, 45, 78, 95],
    "Science": [80, 95, 50, 85, 92],
    "English": [75, 88, 55, 80, 90]
}

df = pd.DataFrame(data)

print(df)

# Calculate total marks
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Calculate average marks
df["Average"] = df["Total"] / 3

print("\nStudent Performance:")
print(df)

# Find topper
topper = df.loc[df["Average"].idxmax()]

print("\nTopper:", topper["Name"])
print("Average Marks:", topper["Average"])

# Pass or Fail Analysis

df["Result"] = np.where(
    df["Average"] >= 50,
    "Pass",
    "Fail"
)

print("\nStudent Results:")
print(df[["Name", "Average", "Result"]])

# Create Seaborn graph
plt.figure(figsize=(8, 5))

sns.barplot(x="Name", y="Average", data=df)

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.show()
df["Result"] = np.where(
    df["Average"] >= 50,
    "Pass",
    "Fail"
)

print(df[["Name", "Average", "Result"]])
# Pass and Fail Pie Chart

result_count = df["Result"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    result_count,
    labels=result_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Pass and Fail Percentage")

plt.show()
# Creating a dataset with missing values
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Riya"],
    "Maths": [85, 90, np.nan, 78, 95],
    "Science": [80, 95, 50, np.nan, 92],
    "English": [75, 88, 55, 80, 90]
}

# Converting the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Displaying the original dataset
print(df)

# Checking which values are missing
print(df.isnull())

# Counting missing values in each column
print(df.isnull().sum())

# Filling missing Maths marks with the average Maths marks
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())

# Filling missing Science marks with the average Science marks
df["Science"] = df["Science"].fillna(df["Science"].mean())

# Displaying the dataset after filling missing values
print(df)

# Removing duplicate rows
df = df.drop_duplicates()

# Displaying the dataset after removing duplicates
print("\nData after removing duplicates:")
print(df)

# Checking missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum())
# Subject-wise Performance Analysis

math_avg = np.mean(df["Maths"])
science_avg = np.mean(df["Science"])
english_avg = np.mean(df["English"])

print("\nSubject-wise Average Marks:")

print("Maths Average:", math_avg)
print("Science Average:", science_avg)
print("English Average:", english_avg)
# Finding the Best Performing Subject

subjects = {
    "Maths": math_avg,
    "Science": science_avg,
    "English": english_avg
}

best_subject = max(subjects, key=subjects.get)

print("\nBest Performing Subject:", best_subject)
# Finding the Lowest Performing Subject

lowest_subject = min(subjects, key=subjects.get)

print("Lowest Performing Subject:", lowest_subject)

# Visualizing Subject-wise Average Marks

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))

sns.barplot(
    x=list(subjects.keys()),
    y=list(subjects.values())
)

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()
# Saving Cleaned Data to CSV File

df.to_csv("cleaned_student_data.csv", index=False)

print("\nCleaned data saved successfully!")
# Reading Data from CSV File

new_df = pd.read_csv("cleaned_student_data.csv")

print("\nReading Data from CSV:")
print(new_df)
# Generating Student Performance Report

report = new_df.copy()

report["Total"] = report["Maths"] + report["Science"] + report["English"]

report["Average"] = report["Total"] / 3

report["Result"] = np.where(report["Average"] >= 50, "Pass", "Fail")

print("\nFINAL STUDENT PERFORMANCE REPORT:")
print(report[["Name", "Total", "Average", "Result"]])
# Calculating Overall Class Average

class_average = report["Average"].mean()

print("\nOverall Class Average:", class_average)