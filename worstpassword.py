import argparse
import random


class WorstPassword:
    __characters = ('0', 'O', 'l', '1', 'I', '|', '5', 'S')
    __min_length = 4
    __max_length = 64

    def __init__(self, length: int = 10):
        if length < WorstPassword.__min_length:
            self._length = WorstPassword.__min_length
        elif length > WorstPassword.__max_length:
            self._length = WorstPassword.__max_length
        else:
            self._length = length

    def generate(self) -> str:
        return ''.join(random.choices(WorstPassword.__characters, k=self._length))


def main():
    parser = argparse.ArgumentParser(description='Generating a worst passwords.')
    parser.add_argument('-l', '--length', type=int, default=10, help='Length of password. Default: 10')
    args = parser.parse_args()
    wp = WorstPassword(args.length)
    print(wp.generate())


if __name__ == '__main__':
    main()
