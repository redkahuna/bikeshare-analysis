import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    
    while True:
        city = input("\nWhich city would you like to filter by? New York City, Chicago, or Washington?\n").title()
        if city in CITY_DATA:
            break
        else:
            print("City not recognized. Please choose from New York City, Chicago, or Washington.")

    while True:
        month = input("\nWhich month would you like to filter by? January, February, March, April, May, June, or type 'all' if you do not have any preference?\n").title()
        if month in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            break
        else:
            print("Month not recognized. Please choose a valid month or 'All'.")

    while True:
        day = input("\nAre you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or type 'all' if you do not have any preference.\n").title()
        if day in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            break
        else:
            print("Day not recognized. Please choose a valid day or 'All'.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    # ... (your existing load_data function remains unchanged)

def time_stats(df):
    # ... (your existing time_stats function remains unchanged)

def station_stats(df):
    # ... (your existing station_stats function remains unchanged)

def trip_duration_stats(df):
    # ... (your existing trip_duration_stats function remains unchanged)

def user_stats(df):
    # ... (your existing user_stats function remains unchanged)

def display_data(df):
    """
    Displays raw data upon user request.
    """
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data != 'yes':
            break
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)  # Add this line to enable viewing raw data

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
