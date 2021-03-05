import argparse
import csv
import Queue
import Server
import Request


def simulateOneServer(file):
    lab_server = Server(file)
    server_queue = Queue()
    waiting_times = []
    counter = 0

    for row in file:
        if Request.timereq == counter:
            request = Request(row)
            server_queue.enqueue(request)

        if (not lab_server.busy()) and (not server_queue.is_empty()):
            next_task = server_queue.dequeue()
            waiting_times.append(next_task.wait_time(row))
            lab_server.start_next(next_task)
            lab_server.tick()

        counter += 1

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait {:.2f} secs {:3d} tasks remaining."
          .format(average_wait, server_queue.size()))


def main(file):
    with open(file, newline='') as f:
        csvData = csv.reader(f)

    simulateOneServer(Server(csvData))


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="File to use", type=str,
                        required=True)
    args = parser.parse_args()
    main(args.file)
