import random

(Mon,Tue,Wed,Thu,Fri,Sat,Sun) = range(0,7)
Wkend = [Sat, Sun]
Wkdys = range(Mon,Sat)
dayMap=("Mon","Tue","Wed","Thu","Fri","Sat","Sun")

class Habit:

    def __init__(self, days, dest, dur, prob=100):
        if isinstance(days,int):
            days = [days]

        self.days = days
        self.dest = dest
        self.dur = dur
        self.prob = prob

    def perform(self, wkday):
        if wkday not in self.days:
            return
        # compute a probability
        doit = random.randint(1,100)
        if doit <= self.prob:
            return (wkday, self.dur, self.dest) 
        return 

    def active(self,wkday):
        return wkday in self.days

