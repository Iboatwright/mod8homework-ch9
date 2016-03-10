# rainfall_program_modification.py
# Exercise selected: Chapter 9 program 3
# Name of program: Rainfall Program Modification
# Description of program: This program allows the user to enter the total
#   rainfall for each month.  It calculates the total rainfall
#   for the year, the average monthly rainfall, and the months with the
#   highest and lowest amounts.  Then it displays the results and an array
#   of the monthly rainfall in ascending order.
#
# Ivan Boatwright
# March 10, 2016

def main():
    # Local constants
    MONTHS = ('january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december')
    HEADERS = ('Rank', 'Rainfall', 'Month')

    # Local variables
    rainfall = []
    yearlyTotal = 0.0
    avgMonthly = 0.0
    lowestMonth = ''
    highestMonth = ''
    monthsByRainfall = []
    rainTable = ''


    # Display intro to user.
    fluffy_intro()

    # Have the user enter the rainfall amount for each month.
    get_rainfall(MONTHS, rainfall)

    # Calculate yearly rainfall total.
    yearlyTotal = sum(rainfall)

    # Calculate average monthly rainfall.
    avgMonthly = calc_average(yearlyTotal, 12)

    # Get an array of (rainfall, month) tuples sorted in ascending order
    monthsByRainfall = merge_sort(rainfall, MONTHS)

    # Get month with the least amount of rain.
    lowestMonth = monthsByRainfall[0][1]

    # Get month with the highest amount of rain.
    highestMonth = monthsByRainfall[-1][1]

    # Get the string to display the sorted array.
    rainTable = tablefy(HEADERS, monthsByRainfall)

    # Display results.
    display_results(yearlyTotal, avgMonthly, lowestMonth, highestMonth,
                    monthsByRainfall, rainTable)
    return None


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Rainfall Statistics program.\n'
          'This program has you enter the total rainfall for each month.\n'
          'It then displays the total rainfall for the year, the monthly\n'
          'average, and the months with the highest and lowest rainfall\n'
          'amounts.\n')
    return None


# Iterates through the list of months.  Each iteration has the user input
#   the rainfall for that month.  The value is assigned to the rainfall array
#   with the same index as that month.
def get_rainfall(MONTHS, rainfall):
    print('{}\nPlease enter the rainfall for each month.\n'.format('_' * 41))
    for month in MONTHS:
        rainfall.append(float(input('{}:  '.format(month.capitalize()))))
    return None


# Calculates the average of two numbers and return the value.  Optionally
#   specify how many decimal places are returned.  If percent is True or if
#   there is no fractional component, the value is converted to an integer
#   and returned.
def calc_average(x, xTotal, precision=2, percent=False):
    avg = round(x / xTotal, precision)
    if percent: avg = '{}%'.format(int(avg * 100))
    elif x % xTotal == 0: avg = int(avg)
    return avg


# Sorts two arrays and returns a list of tuple pairs.  The arrays are
#   sorted by the first parameter in ascending order.
def merge_sort(first, second):
    return sorted(zip(first, second))


# Takes a set of headers, a merged parallel array and optionally a format
#   string and returns a print friendly string.
def tablefy(headers,data,design='{: >9}{:^6} | {:^8} |  {:<11}\n'):
    head = design.format('',*headers)
    division = '{}{}\n'.format(' '*10,'-'*30)
    body = ''.join([design.format('', i+1, j[0], j[1].capitalize())
                    for i, j in enumerate(data)])
    return '{}{}{}'.format(head, division, body)


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(total, avg, least, most, ordered, table):
    print('{}\n'.format('_' * 50))
    print('The total rainfall for the year is: {}'.format(total))
    print('The average monthly rainfall is: {}'.format(avg))
    print('The month with the least rain was: {}'.format(least.capitalize()))
    print('The month with the most rain was: {}'.format(most.capitalize()))
    print('The months in order of least to most rain are:')
    print(table)
    return None


# Start the program.
main()

