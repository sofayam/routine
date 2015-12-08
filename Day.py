class Day:

    def __init__(self, wkday, habits):
        for habit in habits:
            habit.perform(wkday)

