import time
import psutil

class PerformanceCal:
    def __init__(self):
        self.startRamUsage = dict(psutil.virtual_memory()._asdict())["used"]
        self.cpuUsage = []
        self.cpuFreq = []
        self.ramUsage = []
        self.executionTime = []
        self.startTime = None
        self.endTime = None

    def startTimer(self):
        self.startTime = time.time()

    def endTimer(self):
        self.endTime = time.time()

    def getStatus(self):
        self.cpuUsage.append(psutil.cpu_percent())
        self.cpuFreq.append(psutil.cpu_freq()[0])
        self.ramUsage.append((dict(psutil.virtual_memory()._asdict())["used"]- self.startRamUsage)/(1024*1024))
        exTime = self.endTime - self.startTime
        self.executionTime.append(exTime)
    
    @staticmethod
    def avg(l):
        try:
            sum = 0
            for i in l:
                sum += i
            avg = sum / len(l)
            return avg
        except:
            return 0

    def getAvgCpuUsage(self):
        return PerformanceCal.avg(self.cpuUsage)

    def getAvgCpuFreq(self):
        return PerformanceCal.avg(self.cpuFreq)

    def getAvgRamUsage(self):
        return PerformanceCal.avg(self.ramUsage)
    
    def getAvgExecutionTime(self):
        return PerformanceCal.avg(self.executionTime)