import time
import pandas as pd
import numpy as np
from datetime import datetime

#SOURCES: I consulted Geeks for Geeks (geeksforgeeks.org), Statology (statology.org), and Stack Overflow (stackoverflow.com) in the writing of this code.

CITY_DATA = { 'chicago': 'chicago.csv',
              'Chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'New York City' : 'new_york_city.csv',
              'washington': 'washington.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city you want to explore:")
    while city.lower() not in ('chicago', 'new york city', 'washington'):
        print("That is not a valid city. Please choose Chicago, New York City, or Washington.")
        city = input("Enter the city you want to explore:")
    if city.lower() in ("chicago", "new york city", "washington" ):
        print("You chose " + city + ".")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month's data do you wish to examine (you may select all as an option)? Please capitalize the month name.")
    while month.lower() not in ('all', 'january', 'february',  'march',  'april', 'may', 'june', 'july', 'august', 'september', 'november', 'december'):
        print("That is not a valid option. Please select any month or type all.")
        month = input("Which month's data do you wish to examine?")
    if month.lower() in ('all', 'january', 'february', 'march', 'april', 'may', 'june',  'july', 'august', 'september', 'november', 'december'):
        print("You chose " + month + ".")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("For which day of the week do you want data (all is an option)? Please capitalize the day name.")
    while day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print("That is not a valid option. Please select a day of the week or type all.")
        day = input("For which day of the week do you want data?")
    if day.lower() in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print("You chose " + day +".")
    

    print('-'*40)
    return city, month, day




def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load in the data
    #city, month, day = get_filters()
    df=pd.read_csv(CITY_DATA[city.lower()])
    
    #change date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #create month column
    df["month"] = df["Start Time"].dt.month
    #print("month after dt.month", df["month"])
    #filter by month
    if month != 'all':
        #convert month to number
        month = datetime.strptime(month, '%B').month
        #print(month)
        #create month column
        #df["month"] = df["Start Time"].dt.month
        #execute filter
        df = df[df['Start Time'].dt.month == month]
    #print("month after filtering", df["month"])
    #create weekday column
    df["weekday"] = df["Start Time"].dt.day_name
    #filter by day
    if day != 'all':
        #print(day)
        
        #execute filter
        df = df[df["weekday"] == day.title()]
   
   # print("df after weekday filtering", df)
    return df

def view_raw(df):
    """
    Asks the user if they want to view the raw data from their selected city, day, and month. It displays the data 5 lines at a time.
    Args: df - the filtered dataframe from load_data
    Returns: nothing
    """
    
    #TO DO ask user if they want to view raw data
    i=0
    while True:
        ask1 = input("\nDo you want to see the raw data (or more raw data) for the city, month(s), and day(s) you selected (yes or no)?")
        if ask1.lower() =='yes':
         i += 1
         print(df.iloc[(i-1)*5:i*5])
        if ask1.lower() not in ('yes', 'no'):
            ask2 = input("\nThat is not a valid response. Please enter yes or no.")    
        elif ask1.lower() =='no':
       
            break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #print("df made it to time stats", df)
    # TO DO: display the most common month
    #pd.mode
    #print(df)
    com_month = df['month']
    com_month = com_month.mode()[0]
    print("The most common month is",  com_month)
    
    # TO DO: display the most common day of week
    #pd.mode
    com_day = df['weekday']
    com_day = com_day.mode()[0]
    print("The most common day is ",  com_day)
    
    # TO DO: display the most common start hour
    #pd.mode
    com_hr = df["Start Time"].dt.hour
    com_hr = com_hr.mode()[0]
    print("The most common hour is ", com_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start = df["Start Station"].mode()[0]
    print("The most common start station is ", com_start)

    # TO DO: display most commonly used end station
    com_end = df["End Station"].mode()[0]
    print("The most common end station is ", com_end)

    # TO DO: display most frequent combination of start station and end station trip
    
    com_trip = (df["Start Station"] + df["End Station"]).mode()[0]
    print("The most common trip is between the following two stations: ", com_trip)
    
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #trip duration
    total_duration = df["Trip Duration"].sum()
    total_minutes = total_duration/60
    print("The sum of the travel times for all customers is ", total_duration, " seconds, which is ", total_minutes, " minutes.")
    

    # TO DO: display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("The mean customer trip duration is ", mean_time, " seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("\nHere are the numbers of different user types:\n", user_types)

    # TO DO: Display counts of gender
    user_gender = df["Gender"].value_counts()
    print("\nHere is a breakdown of the number of users by gender:\n", user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    oldest = df["Birth Year"].min()
    print("\nThe oldest user was born in the following year:\n", oldest)
    
    youngest = df["Birth Year"].max()
    print("\nThe youngest user was born in the following year:\n", youngest)
    
    most_yr = df["Birth Year"].mode()[0]
    print("\nThe most common birth year of users is the following year:\n", most_yr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        view_raw(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

