#!/bin/bash
LATEX=~/texmf/tex/latex/notexbook

echo "Copying the files to $LATEX..."
mkdir -p -v $LATEX
cp -rf -v src/fi-notexbook-full.sty $LATEX
cp -rf -v src/en-notexbook-full.sty $LATEX
echo "Updating the indexes..."
texhash ~/texmf
