#!/bin/bash
echo "Copying the files to ~/texmf/tex/latex/..."
mkdir -p ~/texmf/tex/latex/notexbook
cp -rf src/notexbook-full.cls ~/texmf/tex/latex/notexbook
cp -rf src/notexbook.sty ~/texmf/tex/latex/notexbook
echo "Updating the indexes..."
texhash ~/texmf
