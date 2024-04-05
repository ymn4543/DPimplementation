import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('healthcare_dataset.csv')

    # Age vs Average billing amount for that age
    bins = np.arange(18, df['Age'].max() + 10, 10)

    # Create age ranges
    df['AgeRange'] = pd.cut(df['Age'], bins, right=False)
    epsilon = 1.0
    delta_f = 100  #
    beta = delta_f / epsilon
    average_billing_by_age_range = df.groupby('AgeRange')['Billing Amount'].mean().reset_index()
    print(average_billing_by_age_range)

    noise = np.random.laplace(0, beta, len(average_billing_by_age_range))
    # Adding noise to the average billing amount
    average_billing_by_age_range['Billing Amount'] += noise
    print(average_billing_by_age_range)

    # Group by AgeRange and calculate average billing amount


    # Gender vs Avg billing amount for that gender
    average_billing_by_gender = df.groupby('Gender')['Billing Amount'].mean().reset_index()
    print(average_billing_by_gender)

    noise = np.random.laplace(0, beta, len(average_billing_by_gender))
    average_billing_by_gender['Billing Amount'] += noise
    print(average_billing_by_gender)


    # Medication vs Avg billing amount for that medication
    average_billing_by_medication = df.groupby('Medication')['Billing Amount'].mean().reset_index()
    print(average_billing_by_medication)
    noise = np.random.laplace(0, beta, len(average_billing_by_medication))
    average_billing_by_medication['Billing Amount'] += noise
    print(average_billing_by_medication)


    # Number of normal diagnosis by age
    normal_diagnoses_by_age_range = df[df['Test Results'] == 'Normal'].groupby('AgeRange').size()
    print("normal diagnosis per age range:", normal_diagnoses_by_age_range)
    noise = np.random.laplace(0, beta, len(normal_diagnoses_by_age_range))
    normal_diagnoses_by_age_range += noise
    print("normal diagnosis per age range:", normal_diagnoses_by_age_range)


    # Number of people who have blood type
    blood_type_counts = df['Blood Type'].value_counts()
    print("Blood type counts:\n", blood_type_counts)
    noise = np.random.laplace(0, beta, len(blood_type_counts))
    blood_type_counts += noise
    print("Blood type counts:\n", blood_type_counts)


main()
