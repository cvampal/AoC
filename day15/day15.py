lines = """Sensor at x=193758, y=2220950: closest beacon is at x=652350, y=2000000
Sensor at x=3395706, y=3633894: closest beacon is at x=3404471, y=3632467
Sensor at x=3896022, y=3773818: closest beacon is at x=3404471, y=3632467
Sensor at x=1442554, y=1608100: closest beacon is at x=652350, y=2000000
Sensor at x=803094, y=813675: closest beacon is at x=571163, y=397470
Sensor at x=3491072, y=3408908: closest beacon is at x=3404471, y=3632467
Sensor at x=1405010, y=486446: closest beacon is at x=571163, y=397470
Sensor at x=3369963, y=3641076: closest beacon is at x=3404471, y=3632467
Sensor at x=3778742, y=2914974: closest beacon is at x=4229371, y=3237483
Sensor at x=1024246, y=3626229: closest beacon is at x=2645627, y=3363491
Sensor at x=3937091, y=2143160: closest beacon is at x=4229371, y=3237483
Sensor at x=2546325, y=2012887: closest beacon is at x=2645627, y=3363491
Sensor at x=3505386, y=3962087: closest beacon is at x=3404471, y=3632467
Sensor at x=819467, y=239010: closest beacon is at x=571163, y=397470
Sensor at x=2650614, y=595151: closest beacon is at x=3367919, y=-1258
Sensor at x=3502942, y=6438: closest beacon is at x=3367919, y=-1258
Sensor at x=3924022, y=634379: closest beacon is at x=3367919, y=-1258
Sensor at x=2935977, y=2838245: closest beacon is at x=2645627, y=3363491
Sensor at x=1897626, y=7510: closest beacon is at x=3367919, y=-1258
Sensor at x=151527, y=640680: closest beacon is at x=571163, y=397470
Sensor at x=433246, y=1337298: closest beacon is at x=652350, y=2000000
Sensor at x=2852855, y=3976978: closest beacon is at x=3282750, y=3686146
Sensor at x=3328398, y=3645875: closest beacon is at x=3282750, y=3686146
Sensor at x=3138934, y=3439134: closest beacon is at x=3282750, y=3686146
Sensor at x=178, y=2765639: closest beacon is at x=652350, y=2000000
Sensor at x=3386231, y=3635056: closest beacon is at x=3404471, y=3632467
Sensor at x=3328074, y=1273456: closest beacon is at x=3367919, y=-1258
Sensor at x=268657, y=162438: closest beacon is at x=571163, y=397470"""

# min_X = 178 max_x = 3937091
# min_Y = 6438 max_Y = 3976978
ll = [ e.split(":") for e in lines.split("\n")]
import random
sensors = []
beacons = []

for l in ll:
    sensor_st = l[0]
    x,y = tuple(sensor_st.split(","))
    sensors.append( ( int(x[12:].strip()), int(y[3:].strip()) ) )
    beacon_st = l[1]
    x,y = tuple(beacon_st.split(","))
    beacons.append(( int(x[24:].strip()), int(y[3:].strip()) ))



dist = lambda x,y : abs(x[0]-y[0]) + abs(x[1]-y[1])

Y = 2000000
pos = set()

for i in range(len(sensors)):
    x,y = sensors[i]
    a,b = beacons[i]
    d = dist((x,y),(a,b))
    dY = dist((x,y),(x,Y))
    if  d >= dY:
        dd = d - dY
        while dd >= 0:
            if ((x-dd,Y) not in beacons):
                pos.add((x-dd,Y))
            if ((x+dd,Y) not in beacons):
                pos.add((x+dd,Y))
            dd -= 1


#from tqdm import tqdm

for _ in range(1000000):
    x = random.randint(178,3937091)
    y = Y#random.randint(0,4_000_000)
    if (x,y) not in pos:
    	if((x,y) not in sensors) and ((x,y) not in beacons):
        	print(x,y)

