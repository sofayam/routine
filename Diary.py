from Day import Day
import csv

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
    def dumpcsv(self):
        with open('%s.csv' % self.name, 'wb') as csvfile:
            csvwriter=csv.writer(csvfile, dialect='excel', delimiter=';')
            for day in self.days:
                day.dumpcsv(csvwriter)
