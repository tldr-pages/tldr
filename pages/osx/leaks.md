# leaks

> Search a process's memory for unreferenced malloc buffers.
> More information: <https://keith.github.io/xcode-man-pages/leaks.1.html>.

- Examine a running process for leaks by its name:

`leaks {{process_name}}`

- Examine a running process for leaks by its PID:

`leaks {{pid}}`

- Launch a command and check for leaks when it exits:

`leaks -atExit -- {{command}}`

- Enable backtraces for each leak by setting the `MallocStackLogging` environment variable:

`MallocStackLogging=YES leaks {{process_name}}`

- Display results in the classic list format instead of a tree:

`leaks -list {{process_name}}`

- Group leaked objects by type:

`leaks -groupByType {{process_name}}`

- Save the memory state to a memory graph file for later analysis:

`leaks {{process_name}} -outputGraph {{path/to/file.memgraph}}`

- Examine a previously saved memory graph file:

`leaks {{path/to/file.memgraph}}`
