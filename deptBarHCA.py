import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("healthcare_analytics_patient_flow_data.csv")

plt.figure()
sns.countplot(y='Department Referral', data=df)

plt.title("Department Referral Distribution")
plt.xlabel("Number of Patients")
plt.ylabel("Department")

plt.show()