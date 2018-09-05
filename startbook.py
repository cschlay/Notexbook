import sys

argv = sys.argv
book_name = argv[1]
author = argv[2]

# Set the path (including directory) to which create a new notebook.
LOCATION = 'C:/' + book_name + '/main.tex'

file = open(LOCATION, 'w+')

content = [
    '\document{notexbook-full}\n\n',
    '\\title{', book_name, '}\n',
    '\\author{', author, '}\n\n',
    '\\begin{document}\n',
    ''.ljust(4), '\maketitle\n',
    ''.ljust(4), '\\tableofcontents\n',
    '\end{document}'
]

for line in content:
    file.write(line)

file.close()
