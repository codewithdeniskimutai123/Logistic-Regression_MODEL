import pandas as pd

# Load the original dataset
df = pd.read_csv("dataset/raw_student_performance.csv")

# Randomly select 1000 rows
df_reduced = df.sample(n=1000, random_state=42)

# Save the reduced dataset
df_reduced.to_csv("reduced_student_performance.csv", index=False)

print("Original dataset size:", df.shape)
print("Reduced dataset size:", df_reduced.shape)

print("Reduced dataset saved as reduced_student_performance.csv")