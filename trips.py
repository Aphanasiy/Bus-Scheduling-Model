import numpy as np


class R50:
    def __init__(self, mean, std):
        def generator(n):
            return np.random.normal(mean, std, n)
        self._generator = generator
    
    def random(self, n):
        return self._generator(n)


class TripGenerator:
    route = None
    disc = None
    speed = None
    def __init__(self, route, discretization=50, speed=20, std=0.3):
        self.route = route
        self.disc = discretization
        self.speed = speed
        self._generator = R50(0.05 / self.speed * 60, std)
    def generate_trip(self):
        timings = []
        time = .0
        dist = 0
        for stop in self.route:
            curdist = stop.dist - dist
            merphy = self._generator.random(-(-curdist // self.disc))
            time += sum(merphy)
            timings.append(time)
            dist = stop.dist
        
        return timings

            

            
            

