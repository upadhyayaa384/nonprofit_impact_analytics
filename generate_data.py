import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

N_PARTICIPANTS = 500

cohorts = ['Virtual Launchpad', 'In-Person Launchpad']
housing_statuses = ['Stably Housed', 'Unstably Housed', 'Correctional/Treatment', 'With Family']
support_areas = ['Housing Assistance', 'Career Counseling', 'Financial Literacy', 'Mental Health']

data = []

for i in range(1, N_PARTICIPANTS + 1):
    modality = np.random.choice(cohorts, p=[0.4, 0.6])

    if modality == 'In-Person Launchpad':
        completion_prob = 0.82
        housing_prob = [0.65, 0.15, 0.05, 0.15]
        employed_prob = 0.75
    else:
        completion_prob = 0.70
        housing_prob = [0.50, 0.25, 0.05, 0.20]
        employed_prob = 0.60

    completed = np.random.choice([1, 0], p=[completion_prob, 1 - completion_prob])
    housing = np.random.choice(housing_statuses, p=housing_prob)
    employed = np.random.choice([1, 0], p=[employed_prob, 1 - employed_prob])
    hub_visits = np.random.poisson(lam=8 if modality == 'In-Person Launchpad' else 4)
    support_needed = np.random.choice(support_areas)
    struggling_rent = 1 if (housing == 'Stably Housed' and np.random.rand() < 0.3) else 0

    data.append({
        'Associate_ID': f"ASC-{1000 + i}",
        'Modality': modality,
        'Program_Completed': completed,
        'Housing_Status': housing,
        'Employed': employed,
        'Hub_Visits_Q3': hub_visits,
        'Primary_Support_Needed': support_needed,
        'Struggling_With_Rent': struggling_rent
    })

df = pd.DataFrame(data)
df.to_csv('synthetic_impact_data.csv', index=False)
print("Dataset successfully generated: synthetic_impact_data.csv")