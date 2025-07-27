# distcc

> Distributed C/C++/ObjC compilation client that works with distccd.
> More information: <https://manned.org/distcc>.

- Compile a source file using a compiler like gcc:

`distcc {{compiler}} -c {{source.c}} -o {{output.o}}`

- Set remote hosts to distribute compilation:

`export DISTCC_HOSTS="localhost {{ip1}} {{ip2}}"`

- Compile a project with make using distcc:

`make -j{{parallel_jobs}} CC="distcc {{compiler}}"`

- Show the list of current distcc hosts:

`distcc --show-hosts`

- Display the version:

`distcc --version`

- Show help:

`distcc --help`
