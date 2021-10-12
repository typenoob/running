import json
from divide import Region
from control import Control
from person import Person
from distance import get_distance_wgs84
import numpy as np
import keyboard as kb
if __name__ == '__main__':
    def start():
        region = Region(config['region'])
        person = Person(config['speed'])
        target = config['target']
        dis_total = 0
        wait_total = 0
        previous = config['region'][0]
        while True:
            record = region.getDivision(config['divide_num'])
            for point in record:
                dis = get_distance_wgs84(previous[1],previous[0],point[1],point[0])
                dis_total += dis
                wait = dis/person.speed
                wait_total += wait
                previous = (point[0],point[1])
                Control.run(wait,previous)
                if dis_total >= target:break
                print('速度(m/s)：',person.speed,'距离(m)：',dis_total,'时间(s)：',wait_total)
            if dis_total >= target:break
        Control.finish()
        print(wait_total/60,dis_total)
    def test():
        region = Region(config['region'])
        flag = False
        #while True:
        record = region.getDivision(config['divide_num'])
        previous = (0, 0)
        count=0
        print('********************')
        for point in record:
            if (count-1)%4==0:print('----------------------')
            count+=1
            print(point[0],point[1],get_distance_wgs84(previous[1],previous[0],point[1],point[0]))
            if get_distance_wgs84(previous[1],previous[0],point[1],point[0])<10:
                flag = True
                break
            previous = point
        if flag:
            print('error')
    def save():
        with open('./config.json','w',encoding='utf8')as fp:
            json.dump(config,fp,ensure_ascii=False)
    with open('./config.json','r',encoding='utf8')as fp:
        config = json.load(fp)
    kb.add_hotkey('f1',start)
    kb.add_hotkey('f2',test)
    kb.add_hotkey('f10',save)
    kb.wait('f8')
    