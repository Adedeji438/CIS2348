def main():
    print("Birthday Calculator")
    print("Current day")
    cur_month = int(input("Month: "))
    cur_day = int(input("Day: "))
    cur_year = int(input("Year: "))
    print("Birthday")
    birth_month = int(input("Month: "))
    birth_day = int(input("Day: "))
    birth_year = int(input("Year: "))

    years = cur_year - birth_year

    if cur_month < birth_month or (cur_day < birth_day and cur_month == birth_month):
        years = years - 1

    print("You are " + str(years) + " years old.")

    if cur_day == birth_day and cur_month == birth_month:
        print("Happy Birthday!")


if __name__ == '__main__':
    main()