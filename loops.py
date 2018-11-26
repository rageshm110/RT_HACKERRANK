#!/bin/python3

##### Task #####

# Read an integer N, for all integer i < N, print i^2 

class HackerRank():
    def loops(self, number):
        self.number = number
        for i in range (0, number):
            print(i**2)

def main():
    number = int(input())

    loop = HackerRank()
    loop.loops(number)
if __name__ == '__main__':
    main()