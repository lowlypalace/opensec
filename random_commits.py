'''
This script augments the dataset with instances of the “negative” class (non-security-relevant) commits.

'''

import subprocess
import os


def random_commits():
    #Listing the repositories cloned in the 'projects' directory.
    path = './projects/'
    projects = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


    #Iterating the list of the projects with 'git log' and collecting commits logs for last 185 commits in each of the repository.
    for x in projects:
        command = 'git -C ./projects/%s log -n 185 --pretty=format:%s,\'"%%H","%%s"\' >> random_commits.csv'
        subprocess.call(command % (x, x), shell='True')

#print(len(projects))
random_commits()
