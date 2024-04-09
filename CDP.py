"""
CS-150 Data Privacy
Youssef, Neelofar, Scott
Privacy Implementation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def main():
    df = pd.read_csv('healthcare_dataset.csv')
    epsilon_values =   [
                        0.01,   # (Very high privacy, very noisy data)
                        0.025,  # (Very high privacy, very noisy data)
                        0.075,  # (High privacy, high noise)
                        0.215,  # (Moderate to high privacy, moderate to high noise)
                        0.65,   # (Moderate privacy, moderate noise)
                        1.65,   # (Low to moderate privacy, low to moderate noise)
                        4.65,   # (Low privacy, low noise)
                        12.75,  # (Very low privacy, very low noise)
                        35.50,  # (Very low privacy, minimal noise)
                        100.00, # (Minimal privacy, minimal noise)]
                       ]

    # Age vs Average billing amount for that age
    # Create age ranges
    bins = np.arange(18, df['Age'].max() + 10, 10)
    df['AgeRange'] = pd.cut(df['Age'], bins, right=False)

    original_average_billing_by_age_range = df.groupby('AgeRange')['Billing Amount'].mean().reset_index()
    # print(original_average_billing_by_age_range)

    average_absolute_errors = []
    average_runtimes = []

    for epsilon in epsilon_values:
        errors = []
        runtimes = []
        for _ in range(10):  # Add noise 10 times
            start_time = time.time()
            noise = np.random.laplace(0, 1 / epsilon, len(original_average_billing_by_age_range))
            noisy_averages = original_average_billing_by_age_range['Billing Amount'] + noise
            elapsed_time = time.time() - start_time
            abs_errors = np.abs(original_average_billing_by_age_range['Billing Amount'] - noisy_averages)
            errors.append(np.mean(abs_errors))
            runtimes.append(elapsed_time)
        average_absolute_errors.append(np.mean(errors))
        average_runtimes.append(np.mean(runtimes))

    # Plotting the error
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_absolute_errors, marker='o')
    plt.xscale('log')
    plt.xlabel('Epsilon (ε)')
    plt.ylabel('Average Absolute Error')
    plt.title('Error vs. Privacy Budget (ε) for average billing amount by age range')
    plt.grid(True, which="both", ls="--")
    plt.show()

    # Plotting the average runtime for each epsilon value
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_runtimes, marker='o', linestyle='-', color='orange')
    plt.xlabel('Epsilon (ε)')
    plt.xscale('log')
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Average Runtime vs. Epsilon (ε) for average billing amount by age range')
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()

    # noise = np.random.laplace(0, beta, len(average_billing_by_age_range))
    # average_billing_by_age_range['Billing Amount'] += noise
    # print(average_billing_by_age_range)




    # Gender vs Avg billing amount for that gender
    average_billing_by_gender = df.groupby('Gender')['Billing Amount'].mean().reset_index()
    print(average_billing_by_gender)

    average_absolute_errors = []
    average_runtimes = []

    for epsilon in epsilon_values:
        errors = []
        runtimes = []
        for _ in range(10):  # Add noise 10 times
            start_time = time.time()
            noise = np.random.laplace(0, 1 / epsilon, len(average_billing_by_gender))
            noisy_averages = average_billing_by_gender['Billing Amount'] + noise
            elapsed_time = time.time() - start_time
            abs_errors = np.abs(average_billing_by_gender['Billing Amount'] - noisy_averages)
            errors.append(np.mean(abs_errors))
            runtimes.append(elapsed_time)
        average_absolute_errors.append(np.mean(errors))
        average_runtimes.append(np.mean(runtimes))

    # Plotting the abs error
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_absolute_errors, marker='o')
    plt.xscale('log')  # Epsilon values span several orders of magnitude
    plt.xlabel('Epsilon (ε)')
    plt.ylabel('Average Absolute Error')
    plt.title('Error vs. Privacy Budget (ε) for average billing amount by gender')
    plt.grid(True, which="both", ls="--")
    plt.show()

    # Plotting the average runtime for each epsilon value
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_runtimes, marker='o', linestyle='-', color='orange')
    plt.xlabel('Epsilon (ε)')
    plt.xscale('log')  # Epsilon values span several orders of magnitude
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Average Runtime vs. Epsilon (ε) for average billing amount by gender')
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()



    # Medication vs Avg billing amount for that medication
    average_billing_by_medication = df.groupby('Medication')['Billing Amount'].mean().reset_index()
    print(average_billing_by_medication)
    # noise = np.random.laplace(0, beta, len(average_billing_by_medication))
    # average_billing_by_medication['Billing Amount'] += noise
    # print(average_billing_by_medication)

    # noise = np.random.laplace(0, beta, len(average_billing_by_gender))
    # average_billing_by_gender['Billing Amount'] += noise
    # print(average_billing_by_gender)
    average_absolute_errors = []
    average_runtimes = []

    for epsilon in epsilon_values:
        errors = []
        runtimes = []
        for _ in range(10):  # Add noise 10 times
            start_time = time.time()
            noise = np.random.laplace(0, 1 / epsilon, len(average_billing_by_medication))
            noisy_averages = average_billing_by_medication['Billing Amount'] + noise
            elapsed_time = time.time() - start_time
            abs_errors = np.abs(average_billing_by_medication['Billing Amount'] - noisy_averages)
            errors.append(np.mean(abs_errors))
            runtimes.append(elapsed_time)
        average_absolute_errors.append(np.mean(errors))
        average_runtimes.append(np.mean(runtimes))

    # Plotting the average abs error
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_absolute_errors, marker='o')
    plt.xscale('log')  # Epsilon values span several orders of magnitude
    plt.xlabel('Epsilon (ε)')
    plt.ylabel('Average Absolute Error')
    plt.title('Error vs. Privacy Budget (ε) for average billing amount per medication')
    plt.grid(True, which="both", ls="--")
    plt.show()

    # Plotting the average runtime for each epsilon value
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_runtimes, marker='o', linestyle='-', color='orange')
    plt.xlabel('Epsilon (ε)')
    plt.xscale('log')  # Epsilon values span several orders of magnitude
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Average Runtime vs. Epsilon (ε) for average billing amount per medication')
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()


    # Number of normal diagnosis by age
    normal_diagnoses_by_age_range = df[df['Test Results'] == 'Normal'].groupby('AgeRange').size()
    print("normal diagnosis per age range:", normal_diagnoses_by_age_range)
    # noise = np.random.laplace(0, 10, len(normal_diagnoses_by_age_range))
    # normal_diagnoses_by_age_range += noise
    # print("normal diagnosis per age range:", normal_diagnoses_by_age_range)
    average_absolute_errors = []
    average_runtimes = []

    for epsilon in epsilon_values:
        errors = []
        runtimes = []
        for _ in range(10):  # Add noise 10 times
            start_time = time.time()
            noise = np.random.laplace(0, 1 / epsilon, len(normal_diagnoses_by_age_range))
            noisy_averages = normal_diagnoses_by_age_range + noise
            elapsed_time = time.time() - start_time
            abs_errors = np.abs(normal_diagnoses_by_age_range - noisy_averages)
            errors.append(np.mean(abs_errors))
            runtimes.append(elapsed_time)
        average_absolute_errors.append(np.mean(errors))
        average_runtimes.append(np.mean(runtimes))

    # Plotting the abs error
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_absolute_errors, marker='o')
    plt.xscale('log')  # Epsilon values span several orders of magnitude
    plt.xlabel('Epsilon (ε)')
    plt.ylabel('Average Absolute Error')
    plt.title('Error vs. Privacy Budget (ε) for count of normal diagnosis by age range')
    plt.grid(True, which="both", ls="--")
    plt.show()

    # Plotting the average runtime for each epsilon value
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_runtimes, marker='o', linestyle='-', color='orange')
    plt.xlabel('Epsilon (ε)')
    plt.xscale('log')  # Epsilon values span several orders of magnitude
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Average Runtime vs. Epsilon (ε) for count of normal diagnosis by age range')
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()


    # Number of people who have each blood type
    blood_type_counts = df['Blood Type'].value_counts()
    print("Blood type counts:\n", blood_type_counts)
    # noise = np.random.laplace(0, beta, len(blood_type_counts))
    # blood_type_counts += noise
    # print("Blood type counts:\n", blood_type_counts)

    average_absolute_errors = []
    average_runtimes = []
    for epsilon in epsilon_values:
        errors = []
        runtimes = []
        for _ in range(10):  # Add noise 10 times
            start_time = time.time()
            noise = np.random.laplace(0, 1 / epsilon, len(blood_type_counts))
            noisy_averages = blood_type_counts + noise
            elapsed_time = time.time() - start_time
            abs_errors = np.abs(blood_type_counts - noisy_averages)
            errors.append(np.mean(abs_errors))
            runtimes.append(elapsed_time)
        average_absolute_errors.append(np.mean(errors))
        average_runtimes.append(np.mean(runtimes))

    # Plotting the abs error
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_absolute_errors, marker='o')
    plt.xscale('log')  # Epsilon values span several orders of magnitude
    plt.xlabel('Epsilon (ε)')
    plt.ylabel('Average Absolute Error')
    plt.title('Error vs. Privacy Budget (ε) for count of blood type')
    plt.grid(True, which="both", ls="--")
    plt.show()

    # Plotting the average runtime for each epsilon value
    plt.figure(figsize=(10, 6))
    plt.plot(epsilon_values, average_runtimes, marker='o', linestyle='-', color='orange')
    plt.xlabel('Epsilon (ε)')
    plt.xscale('log')  # Epsilon values span several orders of magnitude
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Average Runtime vs. Epsilon (ε) for count of blood type')
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()

main()
