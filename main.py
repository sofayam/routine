from Habit import Habit, Wkdys, Wkend, Mon, Tue, Wed, Thu, Fri, Sat, Sun
from Diary import Diary



habits = [
    Habit(Wkdys, "work", 9, 8, 95),
    Habit(Wed, "shopping", None, 1, 50),
    Habit(Thu, "shopping", None, 1, 50),
    Habit(Wkend, "sport", 13, 2, 50),
]

diary = Diary("mark", 28, habits)

diary.dump()
