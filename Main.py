from divide import Region
from control import Control
from person import Person
from distance import get_distance_wgs84
import numpy as np
import keyboard as kb
if __name__ == '__main__':
    def start():
        region = Region([(30.321686, 120.36315), (30.320171, 120.36396)])
        target = 3100
        dis_total = 0
        wait_total = 0
        previous = (30.321686, 120.36315)
        while True:
            record = region.getDivision(16)
            print(record)
            for point in record:
                print(wait_total,dis_total)
                dis = get_distance_wgs84(previous[1],previous[0],point[1],point[0])
                dis_total += dis
                wait = dis/Person.speed
                wait_total += wait
                previous = (point[0],point[1])
                Control.run(wait,previous)
                if dis_total >= target:break
            if dis_total >= target:break
        Control.finish()
        print(wait_total/60,dis_total)
    kb.add_hotkey('f1',start)
    kb.wait()
    