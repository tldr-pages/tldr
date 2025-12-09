# pip wheel

> Build wheel archives for packages and dependencies.
> More information: <https://pip.pypa.io/en/stable/cli/pip_wheel/>.

- Build a wheel for a package:

`pip wheel {{package}}`

- Build wheels for packages in requirements file:

`pip wheel {{[-r|--requirement]}} {{path/to/requirements.txt}}`

- Build wheel to a specific directory:

`pip wheel {{package}} {{[-w|--wheel-dir]}} {{path/to/directory}}`

- Build wheel without dependencies:

`pip wheel {{package}} --no-deps`

- Build wheel from local project:

`pip wheel {{path/to/project}}`

- Build wheel from Git repository:

`pip wheel git+{{https://github.com/user/repo.git}}`
