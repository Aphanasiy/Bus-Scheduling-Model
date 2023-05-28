#!/usr/bin/python3

import graphify
from trips import TripGenerator
import statistics
import routes
import sys

class Params:
    V0 = 25
    Va = 25
    STD = 0.05
    N = 30


curroute = routes.Route(routes.r627k_stops, speed=Params.V0, name="627к")

# sys.exit(0)

base_picture, stats = graphify.generate_graph_base(curroute)
base_picture[0].canvas.manager.set_window_title(f'{curroute.name}-{Params.V0}-{Params.Va}-{Params.STD}')


tgen = TripGenerator(curroute, speed=Params.Va, std=Params.STD)
trips = []
for i in range(Params.N):
    tm = tgen.generate_trip()
    trips.append(tm)
    picture = graphify.add_trip(*base_picture, curroute, tm, "improved", stats)
    picture = graphify.add_trip(*base_picture, curroute, tm, "classic", stats)


poststats = []
for dst, stat in sorted(stats.items())[1:]:
    classmean = statistics.mean(stat['classic']) - stat['Stop'].scheduled
    classdev = statistics.stdev(stat['classic'])
    suggmean = statistics.mean(stat["improved"]) - stat["Stop"].scheduled
    suggdev = statistics.stdev(stat["improved"])
    print("=== === ===")
    print("DST:", dst)
    print(f"""\
CLASSIC:
   MEAN: {classmean}
   STDEV: {classdev}""")
    print(f"""\
SUGGEST:
   MEAN: {suggmean}, 
   STDEV: {suggdev}""")
    poststats.append([
            round(classmean, 4),
            round(classdev, 4), 
            round(suggmean, 4), 
            round(suggdev, 4)
        ])
print(Params.V0, Params.Va, Params.STD, sep='\t')
for i in poststats:
    print(*i, sep='\t')

graphify.show()




