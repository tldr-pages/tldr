# uv pip

> Provides pip-like commands for installing, uninstalling, and managing packages.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-pip>.

- Install a package:

`uv pip install {{package}}`

- Install packages from a requirements file:

`uv pip install {{[-r|--requirements]}} {{requirements.txt}}`

- Install a package with a specific version:

`uv pip install {{package==1.2.3}}`

- Uninstall a package:

`uv pip uninstall {{package}}`

- Save installed packages to file:

`uv pip freeze > {{requirements.txt}}`

- List installed packages:

`uv pip list`

- Show information about an installed package:

`uv pip show {{package}}`

- Sync environment with a requirements file (install/uninstall to match exactly):

`uv pip sync {{requirements.txt}}`
