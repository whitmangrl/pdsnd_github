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
    while True:
        city = input('\nEnter a city chicago, new york city or washington?\n').lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('Invalid! try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nEnter a month from "january to june" Or type "all" to all?\n').lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print('Invalid! try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Enter a day OR Type "all" for all?\n').lower()
        if day in ('all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
            break
        else:
            print('Invalid! try again')


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        m = months.index(month) +1
        df = df[df['month'] == m ]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common momnt: ', df['month'].mode()[0])
    # TO DO: display the most common day of week
    print('\nThe most common day: ', df['day'].mode()[0])
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nThe most common start hour: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most commonly used start station: ', df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station:', df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe combination of start station and end station trip: ', (df['Start Station'] + " & " + df['End Station']).mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nThe total travel time: ', df['Trip Duration'].sum())
    # TO DO: display mean travel time
    print('\nThe mean travel time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe counts odf users types: ', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
          print('\The counts of gender: ', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
          print('\nThe earliest year of birth : ', df['Birth Year'].min())
          print('\nThe most recent year of birth : ', df['Birth Year'].max())
          print('\nThe most common year of birth :', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_data(df):
    d = 0
    while True:
        view = input('\nWould you like to see the next five rows of data? "y" OR "n"\n').lower()
        if view == 'y':
            print(df[d:d+5])
            d += 1
        elif view == 'n':
            break
        else:
            print('invalid input! enter "y" Or "n"')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
