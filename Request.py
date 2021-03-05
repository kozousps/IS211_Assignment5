class Request:
    def __init__(self, time):
        self.timestamp = time
        self.timereq = run_time

    def get_stamp(self):
        return self.timestamp

    def get_timereq(self):
        return self.timereq

    def wait_time(self, current_time):
        return current_time - self.timestamp
