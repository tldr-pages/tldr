# pycodestyle

> A tool to check Python code against PEP 8 style conventions.
> More information: <https://pycodestyle.readthedocs.io>.

- Check the style of a single file:

`pycodestyle {{path/to/file.py}}`

- Check the style of multiple files:

`pycodestyle {{path/to/file1.py}} {{path/to/file2.py}} {{path/to/file3.py}}`

- Show only the first occurrence of an error:

`pycodestyle --first {{path/to/file.py}}`

- Show the source code for each error:

`pycodestyle --show-source {{path/to/file.py}}`

- Show the specific PEP 8 text for each error:

`pycodestyle --show-pep8 {{path/to/file.py}}`
