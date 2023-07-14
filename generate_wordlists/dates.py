from datetime import date


def check_leap_year(year):
    """Checks if a year is a leap year."""
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
    return False


def generate():
    """
    Generates a wordlist with dates from the last 60 years.
    """
    current_year = date.today().year

    with open('../wordlists/dates.txt', 'w') as file:
        for year in range(current_year - 60, current_year + 1):
            for month in range(1, 13):
                if month in (1, 3, 5, 7, 8, 10, 12):
                    for day in range(1, 32):
                        file.write(f'{day:02d}{month:02d}{year}\n')
                elif month in (4, 6, 9, 11):
                    for day in range(1, 31):
                        file.write(f'{day:02d}{month:02d}{year}\n')
                elif month == 2:
                    if check_leap_year(year):
                        for day in range(1, 30):
                            file.write(f'{day:02d}{month:02d}{year}\n')
                    else:
                        for day in range(1, 29):
                            file.write(f'{day:02d}{month:02d}{year}\n')

