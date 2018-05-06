import time


class Task:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.start_time = time.time()
        self.end_time = self.start_time + duration

    @property
    def time_left(self):
        pass
