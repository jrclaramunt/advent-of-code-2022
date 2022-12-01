import argparse

from utils.day_factory import DayFactory


parser = argparse.ArgumentParser()
parser.add_argument('--day', type=int, help='Day')
parser.add_argument('--test', type=bool, nargs='?', const=True,
                    default=False, help='Use test data')

args = parser.parse_args()


if __name__ == '__main__':

    day = args.day

    if args.test:
        input_path = f'test/day{day}.txt'
    else:
        input_path = f'input/day{day}.txt'
    try:
        with open(input_path, 'r') as f:
            input_data = f.readlines()
            DayFactory(day, input_data, vars(args))
    except FileNotFoundError:
        print(f'No data found in {input_path} for Day {day}')

