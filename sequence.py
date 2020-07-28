class Sequence:
    def __init__(self, start, updater):
        self.current = start
        self.updater = updater
    
    def gen(self):
        tmp = self.current
        self.current = self.updater(self.current)
        return tmp