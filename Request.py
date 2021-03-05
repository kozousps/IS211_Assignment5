class Request:
    def __init__(self, time, file):
        self.timestamp = time
        for row in file:
            self.timereq = row[0]

    def get_stamp(self):
        return self.timestamp

    def get_timereq(self):
        return self.timereq

    def wait_time(self, current_time):
        return current_time - self.timestamp
