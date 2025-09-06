# pypy

> Fast and compliant alternative implementation of the Python language.
> More information: <https://doc.pypy.org>.

- Start a REPL (interactive shell):

`pypy`

- Execute script in a given Python file:

`pypy {{path/to/file.py}}`

- Execute script as part of an interactive shell:

`pypy -i {{path/to/file.py}}`

- Execute a Python expression:

`pypy -c "{{expression}}"`

- Run library module as a script (terminates option list):

`pypy -m {{module}} {{arguments}}`

- Install a package using pip:

`pypy -m pip install {{package}}`

- Interactively debug a Python script:

`pypy -m pdb {{path/to/file.py}}`
