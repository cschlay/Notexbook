# Copyright (c) 2018 C. H. Lay
import sys
import os

# Ask Basic Informations
print("Fill the Details.")

print("Language [1] Finnish, [2] English:")
print("Document type [1] Book, [2] Standalone Article:")


print("Title:")
title = input()

print("Author:")
author = input()

#print("File location (defaults to scripts/notexbooks/):")
#directory = input()
ROOT = "notexbooks/{}".format(title)

if not os.path.exists(ROOT):
    os.makedirs(ROOT)

# Standard Structure
LINES = [
    "\\documentclass{book}\n\n",
    "\\usepackage{standalone}\n",
    "%\\usepackage{fi-notexbook-full}\n",
    "\\title{{{}}}\n".format(title),
    "\\author{{{}}}\n".format(author),
    "\n\\begin{document}\n",
    "\\maketitle\n",
    "\\tableofcontents\n"
    "\\end{document}\n"
]

file = open(ROOT + '/main.tex', 'w+')

for line in LINES:
    file.write(line)
file.close()

print("New book initialized at " + ROOT)