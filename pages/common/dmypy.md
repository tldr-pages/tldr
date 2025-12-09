# dmypy

> Type check Python code, running `mypy` as a daemon for better speed.
> See also: `mypy` for more options to use with check and run.
> More information: <https://mypy.readthedocs.io/en/stable/mypy_daemon.html>.

- Type check a file, and start the daemon if it is not running:

`dmypy check -- {{path/to/file.py}}`

- Start the daemon:

`dmypy start`

- Type check a file (requires the daemon to be running):

`dmypy run -- {{path/to/file.py}}`

- Stop the daemon:

`dmypy stop`
