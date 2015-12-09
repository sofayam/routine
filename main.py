from Habit import Habit, Wkdys, Wkend, Mon, Tue, Wed, Thu, Fri, Sat, Sun
from Diary import Diary



habits = [
    Habit(Wkdys, "sport", 1, 20),
    Habit(Wkdys, "work",  8),
    Habit(Wed, "sport", 1),
    Habit(Wed, "shopping",  1, 50),
    Habit(Thu, "shopping",  1, 50),
    Habit(Fri, "mosque", 1),
    Habit(Wkend, "sport",  2, 50),    
]

diary = Diary(name="mark", length=28, startloc="home", wake=9)

diary.fill(habits)

diary.dump()
