import numpy as np
import pandas as pd

def main():
    # beta = 1
    df = pd.read_csv('healthcare_dataset.csv')
    # noise = np.random.laplace(0, beta, df['Room Number'].size)
    # df['Room Number'] += noise

    # noise = np.random.laplace(0, beta, df['Billing Amount'].size)
    # df['Billing Amount'] += noise

    # age_noise = np.random.laplace(0, beta, df['Age'].size)
    # df['Age'] += age_noise

    # # Display the updated DataFrame
    # print(df['Age'])

    # df.to_csv('noisy_healthcare_dataset.csv', index=False)


    # Age vs Avg billing amount for that age
    # Define age bins starting from 18 with a step you prefer, e.g., 10-year ranges
    bins = np.arange(18, df['Age'].max() + 10, 10)  # Adjust the step and max value as needed

    # Create age ranges
    df['AgeRange'] = pd.cut(df['Age'], bins, right=False)

    # Group by AgeRange and calculate average billing amount
    average_billing_by_age_range = df.groupby('AgeRange')['Billing Amount'].mean().reset_index()
    print(average_billing_by_age_range)

    # Gender vs Avg billing amount for that gender
    average_billing_by_gender = df.groupby('Gender')['Billing Amount'].mean().reset_index()
    print(average_billing_by_gender)

    # Medication vs Avg billing amount for that medication
    average_billing_by_medication = df.groupby('Medication')['BillingAmount'].mean().reset_index()
    print(average_billing_by_medication)

    # Number of normal diagnosis
    normal_diagnoses_count = df[df['Medical Condition'] == 'Normal'].shape[0]
    print("Number of normal diagnoses:", normal_diagnoses_count)

    # Number of people who have blood type O, both + and - 
    number_of_people_with_blood_type_O = df[df['Blood Type'].str.startswith('O')].shape[0]



main()
