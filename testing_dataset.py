'''
This script creates the dataset with instances of the testing data.
We log the data about n last commits in each repository available in the 'projects' directory.


'''

import subprocess
import os

def testing_dataset():

    #Listing the repositories cloned in the 'projects' directory.
    path = './projects/'
    projects = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

    #Iterating the list of the projects with 'git log' and collecting commits logs for each of the repository.
    for x in projects:
        command = 'git -C ./projects/%s log -n 1000 --pretty=format:%s,\'"%%H","%%s"\' | sed 1,185d >> testing_dataset.csv'
        subprocess.call(command % (x, x), shell='True')

testing_dataset()
