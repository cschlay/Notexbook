# NotexBook
To speed up self-studying and organizing texts in that would otherwise rest in a paper notebook.

This actually a LaTeX package.

## Prerequisites
As we do not support paper to LaTeX conversion notepads, one must write their notes with LaTeX.

## Installation
You can also use the files directly like placing them in you LaTeX project.

### TexLive (Windows 10)
1. Open file **C:\texlive\2018\texmf.cnf**. The installation path may differ.
2. Add **TEXMFLOCAL = C:\texlive\texmf-local** to the file.
3. Copy the notexbook files from **src** to **C:/texlive/texmf-local/tex/latex/base**. If you know what to do then you can create the necessary directories or place then wherever you want.
4. Run **texhash** in command prompt.
5. Try to compile an example in **examples** folder.


## License
The "docs" and "examples" folders are licensed under [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The rest are under [MIT License](https://choosealicense.com/licenses/mit/).