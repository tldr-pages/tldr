# autopep8

> Formatați codul Python conform ghidului de stil PEP 8.
> Mai multe informaţii: <https://github.com/hhatto/autopep8>

- Formatarea unui fișier la stdout, cu o lungime maximă particularizată a liniei:

`autopep8 {{path/to/file.py}} --max-line-length {{length}}`

- Formatați un fișier, afișând o diff a modificărilor:

`autopep8 --diff {{path/to/file}}`

- Formatați un fișier în ritm și salvați modificările:

`autopep8 --in-place {{path/to/file.py}}`

- Formatați recursiv toate fișierele într-un director în loc și salvați modificările:

`autopep8 --in-place --recursive {{path/to/directory}}`
