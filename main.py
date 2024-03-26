# To run use command python main.py <lambda_rate> <average_service_time>
# Where <lambda_rate> is between 10 and 30 and <average_service_time> is between 0.01 and 0.04.
import sys
from simulator import Simulator

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <lambda_rate> <average_service_time>")
        sys.exit(1)

    try:
        lambda_rate = float(sys.argv[1])
        average_service_time = float(sys.argv[2])

        if lambda_rate < 10 or lambda_rate > 30 or average_service_time < 0.01 or average_service_time > 0.04:
            raise ValueError
    
    except ValueError:
        print("Invalid input. <lambda_rate> must be between 0 and 30 and <average_service_time> between 0.01 and 0.04.")
        sys.exit(1)

    simulator = Simulator(lambda_rate, average_service_time)
    simulator.run()

if __name__ == "__main__":
    main()
