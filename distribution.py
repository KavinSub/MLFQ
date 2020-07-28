from math import ceil
import random

class Uniform:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def sample(self):
        return random.randint(self.lower, self.upper)

class Normal:
    def __init__(self, mean, variance):
        self.mean = mean
        self.variance = variance
    
    def sample(self):
        return ceil(random.normalvariate(self.mean, self.variance))

class Constant:
    def __init__(self, constant):
        self.constant = constant

    def sample(self):
        return self.constant