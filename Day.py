from Trip import Trip
import random
class Day:

    def __init__(self, date, habits, wake, startloc):
        self.trips = []
        self.date = date
        self.day = date % 7
        somethingHappened = False
        loc = startloc
        time = wake
        for habit in habits:
            if habit.active(self.day):
                res = habit.perform(self.day)
                if res:
                    (day,dur,dest) = res
                    if isinstance(dest,tuple):
                        destroot,limit = dest
                        dest = destroot + str(random.randint(1,limit)) 
                    if habit.start:
                        if time == wake:
                            # getting up late
                            time = habit.start
                    if habit.insert:
                        self.trips.append(Trip(loc,day,habit.insert,dest))
                        self.trips.append(Trip(dest,day,habit.insert+dur,loc))
                        time=max(time,habit.insert+dur+1) # insert a buffer in case of late lunch
                        continue
                    somethingHappened = True
                    # only add habits that fire
                    self.trips.append(Trip(loc,day,time,dest))
                    loc = dest
                    time += dur
        if somethingHappened:
            # final trip added back to starting location
            self.trips.append(Trip(loc,day,time, startloc))
            
    def dumpcsv(self, csvwriter):
        if self.trips:
            for trip in self.trips: trip.dumpcsv(csvwriter)

    def dump(self):
        if self.trips:
            for trip in self.trips: trip.dump()
