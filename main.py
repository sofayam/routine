from Habit import Habit, Wkdys, Wkend, Mon, Tue, Wed, Thu, Fri, Sat, Sun
from Diary import Diary
import random

random.seed(0)


habits = [
    Habit(days=Wkdys, dest="sport",        dur=1, prob=90),
    Habit(days=Wkdys, dest="work",         dur=8),
    Habit(days=Wed,   dest="sport",        dur=1),
    Habit(Wed,        dest="shoppingMall", dur=1, prob=50),
    Habit(Thu,        dest="supermarket",  dur=1, prob=50),
    Habit(Fri,        dest="mosque",       dur=1),
    Habit(Wkend,      dest="sport",        dur=2, prob=50, start=12),    
]

diary = Diary(name="mark", length=7, startloc="home", wake=9)




diary.fill(habits)

diary.dump()
diary.dumpcsv()
