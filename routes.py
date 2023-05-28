from stops import Stop, KeyStop
from typing import List

class Route:
    stops: List[Stop] = None
    def __init__(self, stops: List[Stop], speed: float=15, name="?"):
        self.stops = stops.copy()
        self.name=name
        for s in self.stops:
            s.scheduled = (s.dist / 1000) / speed * 60

    
    def __getitem__(self, key):
        return self.stops[key]
    
    def __repr__(self):
        return ("Route[" + "{}, " * (len(self.stops) - 1) + "{}]").format(*self.stops)



r627k_stops = [
    KeyStop(0),
    Stop(250),
    Stop(600),
    Stop(850),
    Stop(1200),
    Stop(1850),
    Stop(2250),
    Stop(2700),
    Stop(3050),
    Stop(3350),
    Stop(3850),
    Stop(4200),
    Stop(4600),
    Stop(5200),
    Stop(5400),
    Stop(5750),
    Stop(6400),
    KeyStop(6900),
    Stop(7400),
    Stop(7950),
    Stop(8600),
    Stop(9050),
    Stop(9300),
    Stop(9500),
    Stop(9850),
    Stop(10600),
    Stop(11450),
    Stop(11700),
    Stop(12050),
    Stop(12350),
    Stop(12850),
    Stop(13200),
    Stop(13450),
    Stop(13750),
    Stop(14150),
    Stop(14450),
    Stop(14700),
    KeyStop(15000)
]


rt41_stops = [
    KeyStop(0),
    Stop(250),
    Stop(550),
    Stop(850),
    Stop(1150),
    Stop(1400),
    Stop(1700),
    Stop(2200),
    Stop(2600),
    Stop(3100), #sch
    Stop(3700),
    Stop(3850),
    Stop(4500),
    Stop(4900),
    Stop(5350),
    Stop(5600),
    Stop(6200),
    Stop(6550),
    Stop(6850),
    Stop(7250),
    Stop(7650),
    Stop(8000),
    Stop(8400),
    Stop(8600), #preobr
    Stop(8950),
    Stop(9450),
    Stop(9850),
    Stop(10400),
    Stop(10800), #sokolniki
    Stop(11300),
    Stop(11800),
    Stop(12200),
    Stop(12800),
    Stop(13500)
]

r223_stops = [
    KeyStop(0),
    Stop(250),
    Stop(700),
    Stop(1050),
    Stop(1350),
    Stop(1700),
    KeyStop(2200),
    Stop(2550),
    Stop(2800),
    Stop(3350),
    KeyStop(3800),
    Stop(4100),
    Stop(4950),
    Stop(5200),
    Stop(5650),
    Stop(5950),
    Stop(6150),
    Stop(6500),
    Stop(6850),
    Stop(7200),
    KeyStop(7750)
]