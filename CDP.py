import numpy as np
import pandas as pd

def main():
    beta = 1
    df = pd.read_csv('healthcare_dataset.csv')
    df_2 = pd.read_csv('healthcare_dataset.csv')
    noise = np.random.laplace(0, beta, df['Room Number'].size)
    df['Room Number'] += noise
    noise = np.random.laplace(0, beta, df['Billing Amount'].size)
    df['Billing Amount'] += noise
    age_noise = np.random.laplace(0, beta, df['ages'].size)
    df['ages'] += age_noise

    # Display the updated DataFrame
    print(df['ages'])





if "__name__" == "__main__":
    main()
