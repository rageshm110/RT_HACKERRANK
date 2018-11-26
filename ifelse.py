#!/bin/python3
#### Task ###
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range  of 6 to 21, print Weird
# If  is even and greater than 20 , print Not Weird

class IfElseTest():
    def test_condition(self, number):
        self.number = number
        if (number % 2 != 0 or (number in range(6, 21) and number% 2 == 0)):
            print("Weird")
        else:
            print("Not weird")

def main():
    number = int(input("Enter the number: "))
    
    test = IfElseTest()
    test.test_condition(number)
if __name__ == '__main__':
    main()