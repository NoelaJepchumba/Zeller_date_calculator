class DateCalculator:

    def __init__(self, year, month, day):
        self.month = month
        self.year = year
        self.day = day

        if month == 1 or month == 2:
            self.month = month + 12
            self.year = year - 1

        self.K = self.year % 100
        self.J = self.year // 100

        self.h = (self.day + (13 * (self.month + 1) // 5) + self.K + (self.K // 4) + (self.J // 4) + (5 * self.J)) % 7

        day_names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.weekday = day_names[self.h]


day=int(input("Enter the day from 1 to 31:"))
month=int(input("Enter the month from 1 to 12:"))
year=int(input("Enter the year:"))
obj = DateCalculator(year,month,day)
print("Day of the week is:", obj.weekday)

#What day of the week was September 15, 1589? It was on a Friday!