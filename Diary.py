class Diary:
    
    def __init__(self, name, length, habits):
        self.days = []
        self.name = name
        for i in range(length):
            wkday = i % 7
            days.append(new Day(wkday, habits))
    def dump(self):
        for day in self.days:
            day.dump()



                     


