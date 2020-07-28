from distribution import Uniform, Normal

import random

class Job:
    def __init__(self, duration, distribution):
        self.duration = duration
        self.distribution = distribution
    
    def run(self, time_slice):
        runtime = min(time_slice, self.distribution.sample(), self.duration)
        self.duration -= runtime
        return runtime
    
    def done(self):
        return self.duration == 0

    @staticmethod
    def randomIOJob():
        dist = Uniform(1, 5 + random.randint(0, 15))
        duration = random.randint(10, 100)

        return Job(duration, dist)

    @staticmethod
    def randomCPUBoundJob():
        dist = Normal(30, 10)
        duration = random.randint(50, 200)

        return Job(duration, dist)