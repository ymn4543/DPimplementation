import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('healthcare_dataset.csv')

    # Age vs Average billing amount for that age
    bins = np.arange(18, df['Age'].max() + 10, 10)

    # Create age ranges
    df['AgeRange'] = pd.cut(df['Age'], bins, right=False)

    # Group by AgeRange and calculate average billing amount
    average_billing_by_age_range = df.groupby('AgeRange')['Billing Amount'].mean().reset_index()
    print(average_billing_by_age_range)

    # Gender vs Avg billing amount for that gender
    average_billing_by_gender = df.groupby('Gender')['Billing Amount'].mean().reset_index()
    print(average_billing_by_gender)

    # Medication vs Avg billing amount for that medication
    average_billing_by_medication = df.groupby('Medication')['Billing Amount'].mean().reset_index()
    print(average_billing_by_medication)

    # Number of normal diagnosis by age
    normal_diagnoses_by_age_range = df[df['Test Results'] == 'Normal'].groupby('AgeRange').size()
    print(normal_diagnoses_by_age_range)

    # Number of people who have blood type
    blood_type_counts = df['Blood Type'].value_counts()
    print("Blood type counts:\n", blood_type_counts)


main()
