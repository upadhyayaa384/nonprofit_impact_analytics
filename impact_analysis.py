import pandas as pd

# Load generated data
df = pd.read_csv('synthetic_impact_data.csv')

# 1. Calculate Employment & Housing Rates by Program Modality
modality_outcomes = df.groupby('Modality').agg(
    Total_Associates=('Associate_ID', 'count'),
    Completion_Rate=('Program_Completed', 'mean'),
    Employment_Rate=('Employed', 'mean'),
    Avg_Hub_Visits=('Hub_Visits_Q3', 'mean')
).reset_index()

print("--- Modality Performance Metrics ---")
print(modality_outcomes)

# 2. Analyze Rent Struggle among Stably Housed Associates
stably_housed = df[df['Housing_Status'] == 'Stably Housed']
rent_struggle_rate = stably_housed.groupby('Modality')['Struggling_With_Rent'].mean().reset_index()

print("\n--- Rent Struggle Rate Among Stably Housed Associates ---")
print(rent_struggle_rate)

# Export summary
modality_outcomes.to_csv('modality_summary.csv', index=False)