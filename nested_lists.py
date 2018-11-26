#!/bin/python3

# #### Task ####

# Given the names and grades for each student in a physics and class of
# N students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with same grade, order their
# names alphabetically and print each name on a new line.
if __name__ == '__main__':
    score_card = list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        score_card.append([name, score])
    print(score_card)


