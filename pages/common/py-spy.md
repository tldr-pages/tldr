# py-spy

> A sampling profiler for Python programs.
> More information: <https://github.com/benfred/py-spy>.

- Show a live view of the functions that take the most execution time of a running process:

`py-spy top {{[-p|--pid]}} {{process_id}}`

- Start a program and show a live view of the functions that take the most execution time:

`py-spy top -- python {{path/to/file.py}}`

- Produce an SVG flame graph of the function call execution time:

`py-spy record {{[-o|--output]}} {{path/to/profile.svg}} {{[-p|--pid]}} {{process_id}}`

- Dump the call stack of a running process:

`py-spy dump {{[-p|--pid]}} {{process_id}}`
