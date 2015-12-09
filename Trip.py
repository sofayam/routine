class Trip:
    def __init__(self,loc,day,time,dest):
        self.loc = loc
        self.day = day
        self.time = time
        self.dest = dest
        

    def dump(self):
        # do your csv magic here
        print "loc: %s, day: %s, time: %s, dest: %s" % (self.loc, self.day, self.time, self.dest)
