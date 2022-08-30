import itertools
import numpy as np
import csv

import pandas


def all_permutation(task_matrix):
    number_of_choice = len(task_matrix)
    solutions = []
    values = []
    for each_solution in itertools.permutations(range(number_of_choice)):
        each_solution = list(each_solution)
        solution = []
        value = 0
        for i in range(len(task_matrix)):
            value += task_matrix[i][each_solution[i]]
            solution.append(task_matrix[i][each_solution[i]])
        values.append(value)
        solutions.append(solution)
    min_cost = np.min(values)
    best_solution = solutions[values.index(min_cost)]
    return min_cost, best_solution


def main():
    n = 0
    datafile = open('Lab #2/input_1.csv', 'r')
    datareader = csv.reader(datafile, delimiter=';')
    for r in datareader:
        n = n + 1
    a = pandas.read_csv("Lab #2/input_1.csv", sep=",",skiprows=1)
    task_matrix = a.drop(a.columns[0], axis=1)
    #
    #task_matrix = []
    for row in datareader:
        #task_matrix.append(row)
        n = n + 1
    for i in task_matrix:
        for j in range(0, n):
            i[j] = int(i[j])
    print(task_matrix)
    min_cost, best_solution = all_permutation(task_matrix)
    print('Назначение задачи для всех способов размещения:')
    print('min cost = ', min_cost)
    print('best solution = ', best_solution)


if __name__ == "__main__":
    main()
