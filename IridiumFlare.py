from datetime import datetime


class IridiumFlare:
    def __init__(self, dataList):
        self.dt = datetime.strptime(dataList[0], '%b %d, %H:%M:%S')
        self.mag = float(dataList[1])
        self.alt = float(dataList[2][:-1])
        self.azi = float(dataList[3][:3])
        self.iriNo = dataList[4]
        self.dis = dataList[5]
        self.magCenter = float(dataList[6])
        self.altSun = float(dataList[7][:-2])
        self.tag = []

    def timeTagging(self, ngtEnd, dwnEnd, mrnEnd, aftEnd, dskEnd):
        if self.dt.time() < datetime.strptime(ngtEnd, "%H:%M:%S").time():
            self.tag.append('ngt')
        elif self.dt.time() < datetime.strptime(dwnEnd, "%H:%M:%S").time():
            self.tag.append('dwn')
        elif self.dt.time() < datetime.strptime(mrnEnd, "%H:%M:%S").time():
            self.tag.append('mrn')
        elif self.dt.time() < datetime.strptime(aftEnd, "%H:%M:%S").time():
            self.tag.append('aft')
        elif self.dt.time() < datetime.strptime(dskEnd, "%H:%M:%S").time():
            self.tag.append('dsk')
        else:
            self.tag.append('ngt')

    def magTagging(self, magCut):
        if self.mag < magCut:
            self.tag.append('brt')
        else:
            self.tag.append('fnt')

    def altTagging(self, altCut):
        if self.alt < altCut:
            self.tag.append('low')
        else:
            self.tag.append('hgh')
