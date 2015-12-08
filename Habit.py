class Habit:
  def __init__(self, wkdays, start, dur, prob):
    self.wkdays = wkdays
    self.start = start
    self.dur = dur
    self.prob = prob
  def perform(self, wkday):
    if wkday not in self.wkdays:
      return
