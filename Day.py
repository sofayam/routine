from Trip import Trip

class Day:

    def __init__(self, date, habits, wake, startloc):
        self.trips = []
        self.date = date
        self.day = date % 7
        active = False
        loc = startloc
        time = wake
        for habit in habits:
            res = habit.perform(self.day)
            if res:
                (day,dur,dest) = res
                active = True
                # only add habits that fire
                self.trips.append(Trip(loc,day,time,dest))
                loc = dest
                time += dur
        if active:
            # final trip added back to starting location
            self.trips.append(Trip(loc,day,time, startloc))
            
    def dump(self):
        if self.trips:
            for trip in self.trips: trip.dump()

