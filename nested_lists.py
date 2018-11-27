#!/bin/python3

# #### Task ####

# Given the names and grades for each student in a physics and class of
# N students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with same grade, order their
# names alphabetically and print each name on a new line.
def get_key(item):
    return item[1]
if __name__ == '__main__':
    score_card = list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        score_card.append([name, score])
    sorted_score_card = sorted(score_card, key=get_key)
    for i in range(0, len(score_card)):
        #print(sorted_score_card[-i][1], ' > ', sorted_score_card[-i-1][1])
        if(sorted_score_card[i][1] < sorted_score_card[i+1][1]):
            runner_up = sorted_score_card[i+1]
            break
        else:
            runner_up = sorted_score_card[0]
    result_set = []
    for i in range(0, len(sorted_score_card)):
        if(sorted_score_card[i][1] == runner_up[1]):
            result_set.append(sorted_score_card[i][0])
    sorted_result_set = sorted(result_set)
    for i in range(0, len(result_set)):
        print(sorted_result_set[i])
    



