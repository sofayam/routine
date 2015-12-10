import Habit

class Trip:
    def __init__(self,loc,day,time,dest):
        self.loc = loc
        self.day = day
        self.time = time
        self.dest = dest
        
    def dumpcsv(self,csvwriter):
        csvwriter.writerow([self.loc, Habit.dayMap[self.day], self.time, self.dest])

    def dump(self):
        # do your csv magic here
        print "loc: %s, day: %s, time: %s, dest: %s" % (self.loc, Habit.dayMap[self.day], self.time, self.dest)
