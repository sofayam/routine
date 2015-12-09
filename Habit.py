

(Mon,Tue,Wed,Thu,Fri,Sat,Sun) = range(0,7)
Wkend = [Sat, Sun]
Wkdys = range(Mon,Sat)

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

