# pip freeze

> Output installed packages. By using `>` the output can be written in a text file.<br>
> More information: <https://pip.pypa.io/en/stable/cli/pip_freeze/>

- Output installed packages:

`python -m pip freeze`

- Output installed packages and write the list in requirements.txt file:

`python -m pip freeze > requirements.txt`

- Output packages installed in a virtual environment, excluding globally-installed packages:

`python -m pip freeze --local > requirements.txt`

- Output packages installed in the user-site:

`python -m pip freeze --user > requirements.txt`

- Output all packages, including pip, distribute, setuptools, and wheel:

`python -m pip freeze --all > requirements.txt`
