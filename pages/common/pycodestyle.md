# pycodestyle

> A tool to check Python code against PEP 8 style conventions.
> More information: <https://pycodestyle.readthedocs.io>.

- Check the style of a single file:

`pycodestyle {{file.py}}`

- Check the style of multiple files:

`pycodestyle {{file1.py}} {{file2.py}} {{file3.py}}`

- Show only the first occurrence of an error:

`pycodestyle --first {{file.py}}`

- Show the source code for each error:

`pycodestyle --show-source {{file.py}}`

- Show the specific PEP 8 text for each error:

`pycodestyle --show-pep8 {{file.py}}`
