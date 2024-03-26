import sys
from simulator import Simulator

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <lambda_rate> <average_service_time>")
        sys.exit(1)

    lambda_rate = float(sys.argv[1])
    average_service_time = float(sys.argv[2])

    simulator = Simulator(lambda_rate, average_service_time)
    simulator.run()

if __name__ == "__main__":
    main()
