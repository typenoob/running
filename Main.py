import json
import os
from divide import Region
from control import Control
from person import Person
from distance import get_distance_wgs84
import numpy as np
import keyboard as kb
if __name__ == '__main__':
    def start():
        region = Region(config['region'])
        person = Person(config['speed']['init'],
                        config['speed']['ave'], config['speed']['step'])
        target = config['target']
        dis_total = 0
        wait_total = 0
        previous = config['region'][0]
        while True:
            record = region.getDivision(config['divide_num'])
            for point in record:
                dis = get_distance_wgs84(
                    previous[1], previous[0], point[1], point[0])
                dis_total += dis
                wait = dis/person.speed
                wait_total += wait
                previous = (point[0], point[1])
                Control.run(wait, previous)
                person.changeSpeed(dis_total/wait_total)
                if dis_total >= target:
                    break
                print('速度:', dis_total/wait_total, person.speed, 'm/s', '距离:',
                      dis_total, 'm', '时间:', wait_total, 's')
            if dis_total >= target:
                break
        Control.finish()
        print('总时间:', wait_total/60, 'min', '总距离:', dis_total /
              1000, 'km', '平均速度:', dis_total/wait_total, 'm/s')

    def test():
        region = Region(config['region'])
        flag = False
        # while True:
        record = region.getDivision(config['divide_num'])
        previous = (0, 0)
        count = 0
        print('********************')
        for point in record:
            if (count-1) % 4 == 0:
                print('----------------------')
            count += 1
            print(point[0], point[1], get_distance_wgs84(
                previous[1], previous[0], point[1], point[0]))
            if get_distance_wgs84(previous[1], previous[0], point[1], point[0]) < 10:
                flag = True
                break
            previous = point
        if flag:
            print('error')

    path = os.environ['runhome']
    with open('%s\config.json' % path, 'r', encoding='utf8')as fp:
        config = json.load(fp)
    print(config['keymap']['start'], ':start')
    print(config['keymap']['test'], ':test')
    print(config['keymap']['stop'], ':stop')
    kb.add_hotkey(config['keymap']['start'], start)
    kb.add_hotkey(config['keymap']['test'], test)
    kb.wait(config['keymap']['stop'])
