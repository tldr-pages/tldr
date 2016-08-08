# pyenv  

> Switch between multiple versions of Python easily.

- List all available commands:

`pyenv commands`

- List all Python versions under the ${PYENV_ROOT}/versions directory:

`pyenv versions`

- Install a Python version(eg: 2.7.10, pypy-2.4.0) under the ${PYENV_ROOT}/versions directory:

`pyenv install {{version}}`

- Uninstall a Python version(eg: 2.7.10, pypy-2.4.0) under the ${PYENV_ROOT}/versions directory:

`pyenv uninstall {{version}}`

- Set Python version(eg: 2.7.10, pypy-2.4.0) to be used globally in the current machine:

`pyenv global {{version}}`

- Set Python version(eg: 2.7.10, pypy-2.4.0) to be used in the current directory and all directories below it:

`pyenv local {{version}}`
