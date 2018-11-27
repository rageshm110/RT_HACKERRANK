if __name__ == '__main__':
    marksheet = list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name, score])
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    # set() - creates unordered collection of unique elelements
    sorted_marksheet = sorted(marksheet)
    for i in range(len(marksheet)):
        if(sorted_marksheet[i][1] == second_highest):
            print(sorted_marksheet[i][0])