import pandas as pd
import numpy as no

def calculate_demographic_data(data_print=True):
    data = pd.read_csv("/content/adult.data.csv")
    #How many people of each race are represented in this dataset?
    amout_of_each_race = data['race'].value_counts()

    #What is the average age of men?
    data_male = data[data['sex'] == "Male"]
    male_average_age = round(np.average(data_male['age']), 1)

    #What is the percentage of people who have a Bachelor's degree?
    bachelor_percentage = round(len(data[data['education'] == "Bachelors"]) / len(data) * 100, 1)

    #What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advance_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advance_education_rich = round(len(advance_education[advance_education['salary'] == ">50K"]) / len(advance_education) * 100,1)

    #What percentage of people without advanced education make more than 50K?
    low_education = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    low_education_rich = round(len(low_education[low_education['salary'] == ">50K"]) / len(low_education) * 100,1)

    #What is the minimum number of hours a person works per week?
    minimum_hour = data['hours-per-week'].min()

    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = data[data["hours-per-week"] == minimum_hour]
    num_min_workers = len(min_workers)

    rich_percentage = round(len(min_workers[min_workers["salary"]==">50K"])/len(min_workers)*100, 1)

    #What country has the highest percentage of people that earn >50K and what is that percentage?
    high_salary = data[data['salary'] == ">50K"].groupby('native-country').count()/data.groupby('native-country').count()
    highest_earning_country = high_salary['salary'].idxmax()

    # the percentage of the highest earning country
    highest_earning_country_percentage = round(len(data[(data["salary"]==">50K") & (data["native-country"]==highest_earning_country)]) / len(data[data["native-country"]==highest_earning_country])*100, 1) # Improved boolean indexing

    #Identify the most popular occupation for those who earn >50K in India.
    india_data = data[data['native-country'] == 'India']
    india_rich_data = india_data[india_data['salary'] == ">50K"]
    india_rich_data = india_rich_data['occupation'].value_counts()
    popular_rich_ocupation_india = india_rich_data.index[0]


    if data_print == True:
        print(f"Number of each race: {amout_of_each_race}")
        print(f"Average age of men: {male_average_age}")
        print(f"Percentage with Bachelors degrees: {bachelor_percentage}%")
        print(f"Percentage with higher education that earn >50K: {advance_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {low_education_rich}%")
        print(f"Minimum working time: {minimum_hour} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print(f"Country with highest percentage of rich: {highest_earning_country}")
        print(f"The percentage of highest rich country: {highest_earning_country_percentage}")
        print(f"Top occupations in India: {popular_rich_ocupation_india}")
    return {
        'race_count': amout_of_each_race,
        'average_age_men': male_average_age,
        'percentage_bachelors': bachelor_percentage,
        'higher_education_rich': advance_education_rich,
        'lower_education_rich': low_education_rich,
        'min_work_hours': minimum_hour,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': popular_rich_ocupation_india
    }
