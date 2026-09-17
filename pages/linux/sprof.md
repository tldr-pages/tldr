# sprof

> Read and display shared object profiling data.
> Note: Requires profile data generated via the `$LD_PROFILE` environment variable.
> More information: <https://manned.org/sprof>.

- Generate a flat profile and call graph (default output):

`sprof {{path/to/library.so}} {{path/to/library.so.profile}}`

- Generate a flat profile with counts and ticks:

`sprof {{[-p|--flat-profile]}} {{path/to/library.so}} {{path/to/library.so.profile}}`

- Generate a call graph:

`sprof {{[-q|--graph]}} {{path/to/library.so}} {{path/to/library.so.profile}}`

- Print call pairs and their usage counts:

`sprof {{[-c|--call-pairs]}} {{path/to/library.so}} {{path/to/library.so.profile}}`

- Use profile data from current directory (auto-detected by soname):

`sprof {{path/to/library.so}}`
