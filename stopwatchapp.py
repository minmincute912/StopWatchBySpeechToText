import time 


class StopWatch:
    def __init__(self):
        self.start_time = None
        self.running = False
        self.elapsed_time = 0.0
    def start(self):
        if not self.running:
            self.start_time = time.perf_counter() - self.elapsed_time
            self.running = True
    def stop(self):
        if not self.running:
            self.start_time = time.perf_counter() - self.elapsed_time
            self.running = False
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0.0
        self.running = False
    def update(self):
        if self.running:
            self.elapsed_time = time.perf_counter() - self.start_time
        minutes = int(self.elapsed_time/60)
        seconds = int(self.elapsed_time - minutes*60.0)
        hundredths = int((self.elapsed_time - minutes*60.0 - seconds)*100)
        
        return "{:02}:{:02}:{:02}".format(minutes, seconds, hundredths)
