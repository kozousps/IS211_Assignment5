class Request:
    def __init__(self, file):
        self.timestamp = file[0]

    def get_stamp(self):
        return self.timestamp

    def wait_time(self, current_time):
        return current_time - self.timestamp
