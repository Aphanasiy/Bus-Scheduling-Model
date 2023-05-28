from stops import Stop, KeyStop

def no_modify(route, trip):

    return trip

def classic_modify(route, trip):
    new_trip = [0]
    delay = 0
    for s, t in zip(route[1:], trip[1:]):
        new_trip.append(max(s.scheduled - 2, t + delay))
        delay += max(0, s.scheduled - 2 - (t + delay))

    # for s, t, nt in zip(route[1:], trip[1:], new_trip[1:]):
    #     print(s, t, nt)
    
    # for relax, time in zip(map(lambda x: 1 if isinstance(x, KeyStop) else 0, route), trip):
    #     delay = min(delay, time + 2)
    #     new_trip.append(time - delay)

    return new_trip

def improved_modify(route, trip):
    new_trip = [0]
    delay = 0
    for s, t in zip(route[1:], trip[1:]):
        new_trip.append(t + delay)
        if isinstance(s, KeyStop):
            delay += max(0, s.scheduled - (t + delay))
    
    return new_trip