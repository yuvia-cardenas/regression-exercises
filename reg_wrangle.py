import pandas as pd
import numpy as np
import os
import env
from env import host, user, pwd

def get_db_url(database):
    return f'mysql+pymysql://{user}:{pwd}@{host}/{database}'
    '''
    Function reads in credentials from env.py file of the user and returns telco data.
    '''

def get_student_data():
    filename = "student_grades.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM student_grades', get_db_url('school_sample'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df

def wrangle_grades():
    '''
    Read student_grades into a pandas DataFrame from mySQL,
    drop student_id column, replace whitespaces with NaN values,
    drop any rows with Null values, convert all columns to int64,
    return cleaned student grades DataFrame.
    '''

    # Acquire data

    grades = get_student_data()

    # Replace white space values with NaN values.
    grades = grades.replace(r'^\s*$', np.nan, regex=True)

    # Drop all rows with NaN values.
    df = grades.dropna()

    # Convert all columns to int64 data types.
    df = df.astype('int')

    return df

