import queue
from process import Process
from event import Event

class Simulator:
    def __init__(self, lambda_rate, average_service_time):
        self.lambda_rate = lambda_rate
        self.average_service_time = average_service_time
        self.clock = 0
        self.CPU_busy = False
        self.event_queue = queue.PriorityQueue()
        self.ready_queue = queue.Queue()

    def run(self):
        # Main loop to run the simulation
        pass

    def generate_process(self):
        # Logic to generate processes
        pass

    def generate_service_time(self):
        # Logic to generate service times for processes
        pass

    # Additional methods for handling events, updating metrics, etc.
