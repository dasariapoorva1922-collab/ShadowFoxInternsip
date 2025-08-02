import pandas as pd
print("Script started...")
# Define weights for each performance metric
weights = {
    "Clean Picks": 1,
    "Good Throws": 1,
    "Catches": 2,
    "Drops": -2,
    "Stumpings": 2,
    "Run Outs": 2,
    "Missed Run Outs": -1,
    "Direct Hits": 2,
    "Runs Saved": 1
}

# File paths
input_path = r"C:\Users\DASARI APOORVA\Desktop\AdvancedLevel\cricket_data.csv"
output_path = r"C:\Users\DASARI APOORVA\Desktop\AdvancedLevel\cricket_performance_results.csv"
print("Reading csv file...")
df = pd.read_csv(input_path)
print("Csv loaded.")
# Calculate performance score
def calculate_score(row):
    total = 0
    for event, weight in weights.items():
        total += row[event] * weight
    return total

df["Performance Score"] = df.apply(calculate_score, axis=1)
df_sorted = df.sort_values(by="Performance Score", ascending=False)

# Save results
print("Saving csv output...")
df_sorted.to_csv(output_path, index=False)

# Confirmation message
print("Cricket performance results saved successfully.")
