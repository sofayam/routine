
Wkdys = range(0,5)
Wkend = range(6,7)
(Mon,Tue,Wed,Thu,Fri,Sat,Sun) = range(0,7)


class Habit:

    def __init__(self, days, loc, start, dur, prob):
        if isinstance(days,int):
            days = [days]

        self.days = days

        self.start = start
        self.dur = dur
        self.prob = prob
        self.loc = loc

    def perform(self, wkday):
        if wkday not in self.days:
            return
        print "performing a habit at %s." % self.loc
