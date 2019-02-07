'''
This script takes the hashes and directories of previously generated commits in 'full_output.csv' and augments the data by collecting statistical data about each commit such as total number of modified files, as well as number of added and deleted lines.

'''

import subprocess
import csv


def patch():
    hash_ = []
    directory = []


    with open("full_output.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            hash_.append(row[2])

    with open("full_output.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            directory.append(row[1])

    hash_.pop(0)
    directory.pop(0)


#Iterating specific commits collected previously and collecting numerical statistics with git show --stat corresponding to each commit.
#Output only the last line of the --stat with tail -n1

    for h, d in zip(hash_, directory):
        command = 'git -C ./projects/%s show %s --stat | tail -n1 >> patch.csv'
        subprocess.call(command % (d, h), shell='True')

patch()
