# Opensec Mining and Classification Tool: Automatic Inference of 'hidden' Security Fixes in Source Code Repositories

The main objective of the software is to automate the search and identification of  commits that introduce fixes to security bugs in open source repositories, that often do not go through public disclosure.

This document gives you basic information on how to start.

## Prerequisites
<ul>
<li>Python 3.6.6 or above
<li>NumPy 1.8.2 or aboveM
<li>SciPy 0.13.3 or above
<li>matplotlib 2.2.3 or above
<li>Pandas 0.23.4 or above
<li>Jupyter notebook
</ul>

## Methods Used
</ul>
<li>Machine Learning
<li>Classification
<li>Data Visualization
<li>Natural Language Processing (NLP)
<li>Data Processing/Cleaning
</ul>


## Dataset collection

For the initial run, you need to populate the `projects` directory with cloned repositories. This can be done by hand, or via `$ git clone` command.

There are several Python scripts used for raw data collection:

`common_vuln_commits.py` script augments the dataset with instances of
the ’positive’ class (security-relevant) commits. The script performs a search over project ’s repositories using regular expression patterns in `etc\keyword_mappings.py`


`cve_id_commits.py` script augments the dataset with instances of the “positive” class (security-relevant) commits. The script performs a search  over project's repositories using regular expression and is able to detect the commits with CVE IDs.

`random_commits.py` script augments the dataset with instances of the “negative” class (non-security-relevant) commits.

`testing_dataset.py` script creates the dataset with instances of the testing data.

`patch.py` script takes the hashes and directories of previously generated commits in `full_output.csv` and augments the data by collecting statistical data about each commit such as total number of modified files, as well as number of added and deleted lines.

The scripts used in the project are both available as individual `.py` files as well as  IPython notebook document `Dataset_Scripts.ipynb`

## Usage


Security fixes can be quite difficult to distinguish based only on the commit message or source code changes statistics. That means that the process of data collection cannot be automated and some manual review such as validation, preprocessing and outliers-detection is needed. The examples of final datasets can be found in `Datasets` directory.

Further, the machine learning models used in this project and their well-documented code can be found in IPython notebook document `ML\Classifier.ipynb`

# Publications

"Automatic Inference of 'hidden' Security Fixes in Source Code Repositories, Daniel Gareev & Stanislav Dashevskiy, University of Luxembourg: [[Paper]](https://github.com/lowlypalace/opensec/raw/master/Automatic%20Inference%20of%20'hidden'%20Security%20Fixes%20in%20Source%20Code%20Repositories.pdf) and [[Presentation]](https://youtu.be/hKUCnciXh0Q)

# License
MIT License, see [license.md](https://github.com/lowlypalace/opensec/blob/master/license.md) for more information.
