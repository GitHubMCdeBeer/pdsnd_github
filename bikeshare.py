#Used as part of Github Project 5 - Refactor Code - Section 4
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    # variable to store city choice
    city = ''
    # get input
    while city not in CITY_DATA.keys():
        print('Please choose city:"\n "Chicago"\n "New York city"\n "Washington"\n')
        city = input().lower()
        #print('selected city:', city)
        if city not in CITY_DATA.keys():
            print("ERROR: Check input. Type City name in full and correctly")

    #print(f'Selected city {city.title()}')

    # TO DO: get user input for month (all, january, february, ... , june)
    # Define month list
    month_list = ['january','february','march','april','may','june','all']
    #variable to store month choice
    month = ''
    # get input
    while month not in month_list:
        print('Please choose month from January to June or all for no filter')
        month = input().lower()
        #print('selected month:', month)
        if month not in month_list:
            print("ERROR: Check input. Type month name in full and correctly else select all")

    # print(f'Selected month {month.title()}')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Define day list
    day_list = {'all','monday','tuesday','wednesday','thursday','saturday','sunday'}
    # variable to store month choice
    day = ''
    # get input
    while day not in day_list:
        print('Please enter day of the week or all for no filter')
        day = input().lower()
        #print('selected day:', day)
        if day not in day_list:
            print("ERROR: Check input. Type day name in full and correctly else select all")

    #print(f'Selected day {day.title()}')

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
    #Load specified city data
    df = pd.read_csv(CITY_DATA[city])
    #Convert dates from strings
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    #Extract date and time parts
    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day'] = df['Start Time'].dt.weekday_name.str.lower()
    df['hour'] = df['Start Time'].dt.hour
    #print(df)
    #print(df['month'])
    #print(df['day'])

    #do month filter if required
    #print('month used to filter:', month)
    if month != 'all':
        df = df[df['month'] == month]
        #print(df)

    #do day filter if required
    #print('day used to filter:',day)
    if day != 'all':
        df = df[df['day'] == day]
        #print(df)

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f'popular month: {popular_month}')

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print(f'popular day: {popular_day}')

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print(f'popular hour: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'popular start station: {popular_start_station}')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'popular end station: {popular_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    #freq_combination = df.corr(method="pearson").max()
    df["combination"] = df["Start Station"] + df["End Station"]
    #print(df)
    popular_combination = df['combination'].mode()[0]
    print(f'popular station combintation: {popular_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    #print(df)
    print(f'Total travel Time: {total_travel_time}')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(f'User type count:\n{user_type_count}')

    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print(f'Gender count:\n{gender_count}')

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = int(df['Birth Year'].min())
    print(f'Earliest birth date: {earliest_birth}')

    latest_birth = int(df['Birth Year'].max())
    print(f'Latest birth date: {latest_birth}')

    most_common_birth_year = int(df['Birth Year'].mode()[0])
    print(f'Most common birth year: {most_common_birth_year}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        counter = 0
        response = ''
        city, month, day = get_filters()
        df = load_data(city, month, day)
        while response != 'yes' and response != 'no':
            print('view raw data? - Yes or No')
            response = input().lower()
            if response == 'yes':
                print(df.head())
                while response == 'yes':
                    #response = ''
                    print('view more raw data? - Yes or No')
                    response = input().lower()
                    counter += 5
                    print(df[counter:counter+5])
            elif print('invalid entry: reselect'):
                response = ''


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
