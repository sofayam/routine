from Habit import Habit, Wkdys, Wkend, Mon, Tue, Wed, Thu, Fri, Sat, Sun
from Diary import Diary
import random

random.seed(0)
runLength = 7

joeHabits = [
    Habit(days=Wkdys, dest="gym",          dur=1, prob=90),
    Habit(days=Wkdys, dest="work",         dur=8),
    Habit(days=Wkdys, dest="lunchPlace",   dur=1, insert=12, prob=20),
    Habit(days=Wkdys, dest="teaShop",      dur=2, insert=17, prob=50),
    Habit(days=Wed,   dest="gym",          dur=1),
    Habit(Wed,        dest="shoppingMall", dur=1, prob=50),
    Habit(Thu,        dest="supermarket",  dur=1, prob=50),
    Habit(Sun,        dest="church",       dur=1, insert=10),
    Habit(Wkend,      dest="sportPlatz",   dur=2, prob=50, start=12),    
]

joeDiary = Diary(name="RegularJoe", length=runLength, startloc="home", wake=9)
joeDiary.fill(joeHabits)
joeDiary.dump()
joeDiary.dumpcsv()




carlHabits = [
    Habit(days=Wkdys, dest=("coffeshop",5),    dur=1, prob=90),
    Habit(days=Wkdys, dest=("work",3),         dur=8),
    Habit(days=Wkdys, dest=("lunchPlace",10),  dur=1, insert=12, prob=20),
    Habit(days=Wkdys, dest="teaShop",      dur=2, insert=17, prob=50),
    Habit(days=Wed,   dest=("nightclub",20),   dur=1),
    Habit(Wed,        dest="shoppingMall", dur=1, prob=50),
    Habit(Thu,        dest="supermarket",  dur=1, prob=50),
    Habit(Sun,        dest=("fruehschoppen",5),  dur=1, insert=10),
    Habit(Wkend,      dest="sportPlatz",   dur=2, prob=50, start=12),        
]

carlDiary = Diary(name="chaoticCarl", length=runLength, startloc="home", wake=9)
carlDiary.fill(carlHabits)
carlDiary.dump()
carlDiary.dumpcsv()
