from Day import Day

class Diary:

    def __init__(self, name, length, startloc, wake):
        self.days = []
        self.name = name
        self.length = length
        self.startloc = startloc
        self.wake = wake
    def fill(self, habits):
        for date in range(self.length):
            self.days.append(Day(date, habits, self.wake, self.startloc))
    def dump(self):
        for day in self.days:
            day.dump()
