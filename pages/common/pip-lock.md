# pip lock

> Lock Python packages and their dependencies into a reproducible file.
> Experimental feature of `pip`.
> More information: <https://pip.pypa.io/en/stable/cli/pip_lock/>.

- Generate a `pylock.toml` for the current project:

`pip lock {{[-e|--editable]}} .`

- Lock dependencies from a requirements file:

`pip lock {{[-r|--requirement]}} {{path/to/requirements.txt}}`

- Specify a custom output file for the lock:

`pip lock {{[-o|--output]}} {{path/to/lockfile.toml}}`

- Lock a specific package and its dependencies:

`pip lock {{package}}`
