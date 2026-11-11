
import pandas as pd

# Create a fictional student dataset
data = {
    "Student ID": ["ST001", "ST002", "ST003", "ST004", "ST005"],
    "Department": [
        "Computer Science",
        "Mathematics",
        "Computer Science",
        "Statistics",
        "Computer Science"
    ],
    "Level": [100, 200, 300, 200, 400],
    "Attendance Percentage": [85, 90, 78, 95, 88],
    "Average Examination Score": [75, 82, 68, 91, 85]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)
