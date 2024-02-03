# pip freeze

> Output installed packages in requirements format.
> More information: <https://pip.pypa.io/en/stable/cli/pip_freeze>.

- List installed packages:

`pip freeze`

- List installed packages and write it to the `requirements.txt` file:

`pip freeze > requirements.txt`

- List installed packages in a virtual environment, excluding globally installed packages:

`pip freeze --local > requirements.txt`

- List installed packages in the user-side:

`pip freeze --user > requirements.txt`

- Output all packages, including `pip`, `distribute`, `setuptools`, and `wheel` (they are skipped by default):

`pip freeze --all > requirements.txt`
