#import the necessary packages
import datetime

class FPS:
    def __init__(self):
        #Store starting and ending time and the total number of frames that were examined
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        #Set the starting time
        self._start = datetime.datetime.now()
        return self
    def stop(self):
        #Set the ending time
        self._end = datetime.datetime.now()
    def update(self):
        self._numFrames += 1
    def elapsed(self):
        return(self._end - self._start).total_seconds()
    def fps(self):
        return self._numFrames / self.elapsed()
