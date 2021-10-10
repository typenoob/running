from random import random


class Region:
    MAX = 0.0001

    def __init__(self, args):
        self.posH = args[0][0]
        self.posV = args[0][1]
        self.spanH = -args[1][0]+args[0][0]
        self.spanV = args[1][1]-args[0][1]

    def shuffleFix(self):
        self.FIXH = self.MAX*(random()-0.5)
        self.FIXV = self.MAX*(random()-0.5)

    def keepInBound(self, args):
        fixh = self.MAX*random()/2
        fixv = self.MAX*random()/2
        if args[0] < self.posH-self.spanH:
            args[0] = self.posH-self.spanH+fixh
        if args[0] > self.posH:
            args[0] = self.posH-fixh
        if args[1] < self.posV:
            args[1] = self.posV+fixv
        if args[1] > self.posV+self.spanV:
            args[1] = self.posV+self.spanV-fixv
        return(args[0], args[1])

    def getDivision(self, num):
        result = []
        footstep = [0]*4
        ave = num//4
        footstep[0] = +self.spanV/ave
        footstep[1] = -self.spanH/ave
        footstep[2] = -self.spanV/ave
        footstep[3] = +self.spanH/ave
        self.shuffleFix()
        now = [self.posH+self.FIXH, self.posV+self.FIXV]
        now = list(self.keepInBound(now))
        for i in range(num):
            result.append([now[0], now[1]])
            self.shuffleFix()
            now[0] += (i//ave % 2)*footstep[i//ave]+self.FIXH
            now[1] += (not i//ave % 2)*footstep[i//ave]+self.FIXV
            now = list(self.keepInBound(now))
        return result
# 下一步计划区域脱出保护机制