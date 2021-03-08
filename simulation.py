import argparse
import csv
from Queue import Queue
from Server import Server
from Request import Request


def simulateOneServer(file):
    """Creates object with csv content in list"""
    with open(file, newline='') as f:
        csvData = list(csv.reader(f))

    total = len(csvData)
    lab_server = Server(csvData)
    server_queue = Queue()
    waiting_times = []

    """When first index matches currentsec, enqueues line to queue"""
    for currentsec in range(total):
        request = Request(csvData)
        if request.timestamp is currentsec:
            server_queue.enqueue(request)

        """
        When server not busy and queue has content, dequeues
        and starts processing
        """
        if (not lab_server.busy()) and (not server_queue.is_empty()):
            next_task = server_queue.dequeue()
            waiting_times.append(next_task.wait_time(currentsec))
            lab_server.start_next(next_task)

    """ Ticks server time"""
    lab_server.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait {:.2f} secs {:3d} tasks remaining."
          .format(average_wait, server_queue.size()))


def simulateManyServer(file, num):
    with open(file, newline='') as f:
        csvData = list(csv.reader(f))

    total = len(csvData)
    lab_server = Server(csvData)
    server_queue = Queue()
    waiting_times = []

    for currentsec in range(total):
        request = Request(csvData)
        if request.timestamp is currentsec and server_queue.is_empty():
            server_queue.enqueue(request)

            """
            Creates another queue for existing servers range(num)
            and enqueues, dequeues, as server_queues fill up.
            """
            while server_queue.size() > 1:
                for i in range(num):
                    server_queue.enqueue(server_queue.dequeue())

                server_queue.dequeue()

            return server_queue.dequeue()

        if (not lab_server.busy()) and (not server_queue.is_empty()):
            next_task = server_queue.dequeue()
            waiting_times.append(next_task.wait_time(currentsec))
            lab_server.start_next(next_task)

    lab_server.tick()


def main(file, num):
    if num == 1:
        simulateOneServer(file)
    else:
        simulateManyServer(file)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="File to use", type=str,
                        required=True)
    parser.add_argument("--server", help="Number of server", type=int,
                        required=False, default=1)
    args = parser.parse_args()
    main(args.file, args.server)
