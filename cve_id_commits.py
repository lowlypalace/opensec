'''
This script augments the dataset with instances of the “positive” class (security-relevant) commits.
The script performs a search  over project's repositories using regular expression and is able to detect the commits with CVE IDs.

'''

import subprocess
import os


def cve_id_commits():
    #Listing the repositories cloned in the 'projects' directory.
    path = './projects/'
    projects = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

    #Iterating the list of the projects with 'git log' and collecting commits logs matching 'CVE-ID' pattern.
    for x in projects:
        command = 'git -C ./projects/%s log --pretty=format:%s,\'"%%H","%%s"\' | grep  -E "(?i)CVE-\d{4}-\d{4,7}" >> cve_id_commits.csv'
        subprocess.call(command % (x, x), shell='True')

cve_id_commits()
