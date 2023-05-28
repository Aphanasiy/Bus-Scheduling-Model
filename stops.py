class Stop:
    dist: float = None
    scheduled: float = None
    def __init__(self, dist):
        self.dist = dist

    def __repr__(self):
        return f"Stop(dist={self.dist}, time={round(self.scheduled, 2)})"

class KeyStop(Stop):
    def __init__(self, dist):
        super().__init__(dist)
    
    def __repr__(self):
        return f"KeyStop(dist={self.dist}, departure_time={round(self.scheduled, 2)})"

