# pipx

> Install and run python applications in isolated environments.
> More information: <https://github.com/pipxproject/pipx>.

- Run an app in a temporary virtual environment:

`pipx run {{pycowsay}} {{moo}}`

- Install a package in a virtual environment and add entry points to path:

`pipx install {{package}}`

- List installed packages:

`pipx list`

- Run an app in a temporary virtual environment with a package name different from the executable:

`pipx run --spec {{httpx-cli}} {{httpx}} {{http://www.github.com}}`
