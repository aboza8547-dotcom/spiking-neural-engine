class ConvergenceCell:

    def __init__(self, epsilon=1e-6):
        self.current = 0.0
        self.previous = 0.0
        self.epsilon = epsilon

    def update(self, value):
        self.previous = self.current
        self.current = value

    def converged(self):
        return abs(self.current - self.previous) < self.epsilon

    def error(self):
        return abs(self.current - self.previous)
