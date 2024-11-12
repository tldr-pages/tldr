# abrt-action-analyze-backtrace

> Analyze C/C++ backtrace.
> Generate duplication hash, backtrace rating, and identify crash function.
> Save the data as new elements `duphash`, `rating`, `crash_function` in the problem directory.
> More information: <https://manned.org/abrt-action-analyze-backtrace>.

- Analyze backtrace for the current working directory:

`abrt-action-analyze-backtrace`

- Analyze backtrace for a specific directory:

`abrt-action-analyze-backtrace -d {{path/to/directory}}`

- Analyze backtrace verbosely:

`abrt-action-analyze-backtrace -v`
