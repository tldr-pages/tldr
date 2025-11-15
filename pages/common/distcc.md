# distcc

> Distributed C/C++/ObjC compilation client that works with `distccd`.
> More information: <https://manned.org/distcc>.

- Compile a source file using a compiler like `gcc`:

`distcc {{gcc}} -c {{path/to/source.c}} -o {{path/to/output.o}}`

- Set remote hosts to distribute compilation:

`export DISTCC_HOSTS="localhost {{ip1 ip2 ...}}"`

- Compile a project with `make` using `distcc`:

`make {{[-j|--jobs]}} {{parallel_jobs}} CC="distcc {{gcc}}"`

- Show the list of current `distcc` hosts:

`distcc --show-hosts`

- Display help:

`distcc --help`

- Display version:

`distcc --version`
