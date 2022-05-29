import pandas as pd
import graphs

pd.set_option('display.max_columns', 8)

general = 'test/general.csv'
prenatal = 'test/prenatal.csv'
sports = 'test/sports.csv'
hospital_type = 'hospital'

# reading input from csv files
general_df = pd.read_csv(general)
prenatal_df = pd.read_csv(prenatal)
sports_df = pd.read_csv(sports)


def generate_df():
    # the column names in all dataframes should match
    prenatal_df.columns = general_df.columns
    sports_df.columns = general_df.columns

    # merge all the dataframes into one large dataframe
    hospitals = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

    # delete the first column which is randomly generated after merge (redundant)
    hospitals.drop(columns=hospitals.columns[0], inplace=True)

    return hospitals


def improvise_df():
    gender_mapper = {'female': 'f', 'male': 'm', 'woman': 'f', 'man': 'm'}
    gender = 'gender'
    zero_columns = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']

    # getting dataset
    hospitals = generate_df()

    # Handling Nan Values
    # delete all the empty rows
    hospitals.dropna(axis='index', how='all', inplace=True)

    # replace the Nan values with f in the prenatal hospital
    hospitals[gender] = hospitals.groupby(hospital_type)[gender].apply(lambda x: x.fillna('f'))

    # replace the Nan values with 0 in the corresponding columns
    hospitals[zero_columns] = hospitals[zero_columns].fillna(0)

    # changing gender values to either 'm' or 'f'
    hospitals.loc[:, gender] = [gender_mapper[gen] if gen in gender_mapper else gen for gen in hospitals[gender]]

    return hospitals


def statistics():
    # getting dataset
    hospitals = improvise_df()

    # determine the hospital with the largest number of patients
    print(" 1. Which hospital has the highest number of patients?")
    print()
    print("     " + str(hospitals[hospital_type].mode()[0]).capitalize())
    print()

    # determine the share of patients in the general hospital that suffer from stomach related issues
    general_patients = hospitals.loc[hospitals.hospital == 'general', :].shape[0]
    general_patients_stomach = \
        hospitals.loc[(hospitals.diagnosis == 'stomach') & (hospitals.hospital == 'general'), :].shape[0]

    print(" 2. What share of the patients in the general hospital suffers from stomach-related issues? ")
    print()
    print("     " + str(round(general_patients_stomach / general_patients, 3)))
    print()

    # determine the share of patients in the sports hospital that suffer from dislocation-related issues
    sports_patients = hospitals.loc[hospitals.hospital == 'sports', :].shape[0]

    sports_patients_dislocation = \
        hospitals.loc[(hospitals.hospital == 'sports') & (hospitals.diagnosis == 'dislocation'), :].shape[0]

    print(" 3. What share of the patients in the sports hospital suffers from dislocation-related issues? ")
    print()
    print("     " + str(round(sports_patients_dislocation / sports_patients, 3)))
    print()

    # find the difference in median ages of the patient in general and the one in sports
    gen_df = pd.read_csv(general)
    sport_df = pd.read_csv(sports)
    gen_median_age = gen_df['age'].median()
    sports_median_age = sport_df['age'].median()

    print(" 4. What is the difference in the median ages of the patients in the general and sports hospitals? ")
    print()
    print("     " + str(gen_median_age - sports_median_age))
    print()

    # find the hospital with the largest number of blood tests
    blood_test_table = pd.pivot_table(hospitals.loc[hospitals.blood_test == 't', :],
                                      index='hospital', values='blood_test', aggfunc='count')
    max_blood_test = blood_test_table.blood_test.max()

    print(""" 5. After data processing at the previous stages, the blood_test column has three values: 
            t = a blood test was taken, 
            f = a blood test wasn't taken, and 
            0 = there is no information. 
        In which hospital the blood test was taken the most often? 
        How many blood tests were taken?""")
    print()
    print("     " + str(blood_test_table.index[blood_test_table['blood_test'] == max_blood_test][0]).capitalize(),
          "had the most with", str(max_blood_test), "blood tests taken.")
    print()


def plotting():
    hospitals = improvise_df()
    graphs.plot_age_histogram(hospitals['age'].tolist())
    graphs.plot_diagnosis_pie_char(hospitals['diagnosis'].tolist())

    # plot the heights
    heights = hospitals.loc[:, 'height'].tolist()
    graphs.plot_height_violin_plot_unified(heights)
    print()
    print("     The answer to the 1st question: 15-35")
    print()
    print("     The answer to the 2nd question: Pregnancy")
    print()
    print("""     The answer to the 3rd question: The gap between values as well as the presence of two peeks
                  can be explained by the use of two different measurement systems. As the height in both prenatal
                  and general is the meter while the sports hospital uses the imperial system: feet where a foot is
                  0.3048 meters""")


if __name__ == '__main__':
    print()
    print("General Hospital Database")
    print()
    print(general_df.sample(n=20, random_state=30))
    print()
    print("Prenatal Hospital Database")
    print()
    print(prenatal_df.sample(n=20, random_state=30))
    print()
    print("Sports Hospital Database")
    print()
    print(sports_df.sample(n=20, random_state=30))
    print()
    print()
    print("Merged Hospital Database")
    print()
    hos = generate_df()
    print(hos.sample(n=20, random_state=30))
    print()
    print("Improved Hospital Database")
    print()
    hos = improvise_df()
    print(hos.sample(n=20, random_state=30))
    print()
    print()
    print("Statistical Analysis of given Hospital Data:")
    print()
    statistics()
    print()
    print("""Plotting and More Analysis:
    
    1. What is the most common age of a patient among all hospitals? 
       Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.

    2. What is the most common diagnosis among patients in all hospitals? 
       Create a pie chart.

    3. Build a violin plot of height distribution by hospitals. 
       What is the main reason for the gap in values? 
       Why there are two peaks, which correspond to the relatively small and big values?""")
    plotting()
