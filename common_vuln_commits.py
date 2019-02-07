'''
This script augments the dataset with instances of the “positive” class (security-relevant) commits.
The script performs a search over project's repositories using regular expression patterns that we created from for the Top 10 OWASP 2018 that are located in 'keyword_mappings'.

'''
import subprocess
import os
from etc.keyword_mappings import vuln_types as mappings

def common_vuln_commits(command):
    for k, j in mappings.items():
        vuln_list = list(j)
        output_list = []
        for x in vuln_list:
            output_list.append("'" + x + "'")

        for e in output_list:
            subprocess.call(command % (i, i, e), shell='True')

#Listing the repositories cloned in the 'projects' directory.
path = './projects/'
projects = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


for index, i in enumerate(projects):
    common_vuln_commits('git -C ./projects/%s log --pretty=format:%s,\'"%%H","%%s"\' | grep -E -w %s >> common_vuln_commits.csv')
