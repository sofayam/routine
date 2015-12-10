from Habit import Habit, Wkdys, Wkend, Mon, Tue, Wed, Thu, Fri, Sat, Sun
from Diary import Diary
import random

random.seed(0)


habits = [
    Habit(days=Wkdys, dest="gym",          dur=1, prob=90),
    Habit(days=Wkdys, dest="work",         dur=8),
    Habit(days=Wkdys, dest="lunchPlace",   dur=1, insert=12, prob=20),
    Habit(days=Wkdys, dest="teaShop",      dur=2, insert=17, prob=50),
    Habit(days=Wed,   dest="gym",          dur=1),
    Habit(Wed,        dest="shoppingMall", dur=1, prob=50),
    Habit(Thu,        dest="supermarket",  dur=1, prob=50),
    Habit(Fri,        dest="mosque",       dur=1),
    Habit(Wkend,      dest="sportPlatz",   dur=2, prob=50, start=12),    
]

diary = Diary(name="rashid", length=7, startloc="home", wake=9)
diary.fill(habits)

diary.dump()
diary.dumpcsv()
