from typing import Optional

input_filename = 'inputDates.txt'
output_filename = 'parsedDates.txt'
months = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6,
          'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12}

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return str(self.month) + '/' + str(self.day) + '/' + str(self.year)

def find(line: str) -> Optional[Date]:
    try:
        parts = line.split(' ')
        if len(parts) != 3:
            raise Exception

        month = -1
        for m in months:
            if m == parts[0].strip():
                month = months[m]

        if month == -1:
            raise Exception

        if parts[1][-1] != ',':
            raise Exception
        day = int(parts[1][0:-1])
        year = int(parts[2])
        return Date(day, month, year)
    except Exception:
        return None

if __name__ == '__main__':
    f = open(input_filename, 'r')
    dates = []
    for line in f.readlines():
        if line.strip() == '-1':
            break
        date = find(line)
        if date is not None:
            dates.append(date)
    f.close()

    out = open(output_filename, 'w')
    for date in dates:
        out.write(str(date) + '\n')
    out.close()