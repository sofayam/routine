class Day:

    def __init__(self, date, habits):
        self.date = date
        self.day = date % 7
        for habit in habits:
            habit.perform(self.day)

    def dump(self):
        print("dump of day %s" % self.date)
