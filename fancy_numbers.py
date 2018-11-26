# #!/bin/python

# Read an integer N.

# Without using any string methods, try to print the following:
# 123...N
# Note that "..." represents the values in between.

def main():
    N = int(input())

    my_list = list(range(1, N+1))
    print(''.join(map(str, my_list)))
if __name__ == '__main__':
    main()