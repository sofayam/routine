from Day import Day

class Diary:

    def __init__(self, name, length, habits):
        self.days = []
        self.name = name
        for date in range(length):
            self.days.append(Day(date, habits))
    def dump(self):
        for day in self.days:
            day.dump()
