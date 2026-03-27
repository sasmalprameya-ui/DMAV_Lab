import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("healthcare_analytics_patient_flow_data.csv")

plt.figure()
plt.hist(df['Patient Age'], bins=20)

plt.title("Patient Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")

plt.show()