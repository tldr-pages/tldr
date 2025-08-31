# uv run

> Run a command or script in the project environment.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-run>.

- Run a Python script:

`uv run {{path/to/script.py}}`

- Run a Python module:

`uv run {{[-m|--module]}} {{module_name}}`

- Run a command with additional packages installed temporarily:

`uv run {{[-w|--with]}} {{package}} {{command}}`

- Run a script with packages from a requirements file:

`uv run --with-requirements {{path/to/requirements.txt}} {{path/to/script.py}}`

- Run in an isolated environment (no project dependencies):

`uv run --isolated {{path/to/script.py}}`

- Run without syncing the environment first:

`uv run --no-sync {{command}}`
