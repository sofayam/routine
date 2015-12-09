
Wkdys = range(0,5)
Wkend = range(6,7)
(Mon,Tue,Wed,Thu,Fri,Sat,Sun) = range(0,7)


class Habit:

    def __init__(self, days, dest, dur, prob):
        if isinstance(days,int):
            days = [days]

        self.days = days
        self.dest = dest
        self.dur = dur
        self.prob = prob

    def perform(self, wkday):
        if wkday not in self.days:
            return
        # TBD probability ???
        return (wkday, self.dur, self.dest) 

