# Data Analysis
A personal project for analyzing given data from 3 hospitals and plotting necessary statistics.
This project involves usage of libraries such as Pandas, Matplotlib and Numpy to process and plot data based on the given information from three hospitals:
- General
- Prenatal
- Sports

The CSV files for the 3 hospitals are in the 'test' folder of the repository.


## Stage 1: Taking Input

Files are added to the test folder in the project folder and loaded into the file using read_csv() method of the pandas module.

Files are then compared and UPDATED so that all the columns match. They are then merged into one single dataset for improving, training and testing. Redundant columns are deleted.


## Stage 2: Improving Dataset

Once the dataset is ready, it is time to process it. To do that, the first step is handling NaN (Not a Number) values. 

- Delete all the empty rows.
- Replace the NaN values in the gender column of the prenatal hospital with f (we can assume that the prenatal treats only women).
- Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns with zeroes.

Once the NaN values are handled, values are corrected and normalized.
Let's take a closer look at the gender column. It's a big mess: there we have female, male, man, woman. You need to correct the data in this column. 
The values should be either f or m. 


## Stage 3: Statistical Analysis

The dataset has been cleared of empty rows and values. Some values have also been corrected, and now we can start a comprehensive study of our data.  In this stage, we will find the main statistical characteristics of our data, consider data distributions, and so on.

These questions will be answered using statistical methods:

- Which hospital has the highest number of patients?
	
    Using mode() function, hospital with the most number of patients is extracted.

- What share of the patients in the general hospital suffers from stomach-related issues? Round the result to the third decimal place?

    Using .loc to locate and filter required data from general hospital and round off value

- What share of the patients in the sports hospital suffers from dislocation-related issues? Round the result to the third decimal place?

   Using .loc to locate and filter required data from sports hospital and round off value

- What is the difference in the median ages of the patients in the general and sports hospitals?
	
   Using median() method to compare.
	
- After data processing at the previous stages, the blood_test column has three values: t= a blood test was taken, f= a blood test wasn't taken, and 0= there is no information. In which hospital the blood test was taken the most often (there is the biggest number of t in the blood_test column among all the hospitals)? How many blood tests were taken?

   Creating a pivot table with values='blood_test' aggfunc='count' to find the hospital with the most blood tests. 

<p align="center"><img src = "./images/stats.png?raw=true" width=66%></p>


## Stage 4: Plotting Values and Extended Analysis

Graphics are arguably the most accessible way to represent the data and its structure. Sometimes, it can help to find the main data patterns and deviations. We will use data visualization methods to conclude our dataset. 

The following graphs will be plotted and the questions will be answered:

- What is the most common age of a patient among all hospitals? Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.
	<p align="center"><img src = "./images/age_hist.png?raw=true" width=66%></p>
	From the plotted histogram, it was found that 15-35 was the most common age group.

- What is the most common diagnosis among patients in all hospitals? Create a pie chart.
	<p align="center"><img src = "./images/pie_chart.png?raw=true" width=66%></p>
	From the generated pie chart, it was found that pregnancy is the most common diagnosis
	
- Build a violin plot of height distribution by hospitals. What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively small and big values?
	<p align="center"><img src = "./images/violin_plot.png?raw=true" width=66%></p>
	The gap between values as well as the presence of two peeks can be explained by the use of two different measurement systems. As the height in both prenatal and general is the meter while the sports hospital uses the imperial system, feet where 1 foot is 0.3048 meters

<p align="center"><img src = "./images/plot_data.png?raw=true" width=66%></p>

