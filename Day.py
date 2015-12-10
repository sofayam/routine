from Trip import Trip

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
                if habit.start:
                    if time == wake:
                        # getting up early
                        time = habit.start
                if res:
                    (day,dur,dest) = res
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
