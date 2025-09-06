# pyenv

> Switch between multiple versions of Python easily.
> See also: `asdf`.
> More information: <https://github.com/pyenv/pyenv>.

- List all available commands:

`pyenv commands`

- List all Python versions under the `${PYENV_ROOT}/versions` directory:

`pyenv versions`

- List all Python versions that can be installed from upstream:

`pyenv install --list`

- Install a Python version under the `${PYENV_ROOT}/versions` directory:

`pyenv install {{2.7.10}}`

- Uninstall a Python version under the `${PYENV_ROOT}/versions` directory:

`pyenv uninstall {{2.7.10}}`

- Set Python version to be used globally in the current machine:

`pyenv global {{2.7.10}}`

- Set Python version to be used in the current directory and all directories below it:

`pyenv local {{2.7.10}}`
