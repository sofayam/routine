from Habit import Habit, Wkdys, Wkend, Mon, Tue, Wed, Thu, Fri, Sat, Sun
from Diary import Diary
import random

random.seed(0)


habits = [
    Habit(days=Wkdys, dest="sport", dur=1, prob=20),
    Habit(days=Wkdys, dest="work",  dur=8),
    Habit(days=Wed, dest="sport", dur=1),
    Habit(Wed, "shopping",  1, 50),
    Habit(Thu, "shopping",  1, 50),
    Habit(Fri, "mosque", 1),
    Habit(Wkend, "sport",  2, 50),    
]

diary = Diary(name="mark", length=28, startloc="home", wake=9)




diary.fill(habits)

#diary.dump()
diary.dumpcsv()
