# uv run

> Run a command or script in the project environment.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-run>.

- Run a Python script:

`uv run {{script.py}}`

- Run a Python module:

`uv run {{[-m|--module]}} {{module_name}}`

- Run a command with additional packages installed temporarily:

`uv run --with {{package}} {{command}}`

- Run a script with packages from a requirements file:

`uv run --with-requirements {{requirements.txt}} {{script.py}}`

- Run in an isolated environment (no project dependencies):

`uv run --isolated {{script.py}}`

- Run without syncing the environment first:

`uv run --no-sync {{command}}`
