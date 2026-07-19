# asprof

> Low-overhead sampling profiler for HotSpot JVMs (async-profiler).
> See also: `jcmd`, `jps`, `pprof`.
> More information: <https://github.com/async-profiler/async-profiler>.

- Profile a Java process for 30 seconds and write a flame graph:

`asprof -d 30 -f {{path/to/flamegraph.html}} {{pid}}`

- Start profiling a running process:

`asprof start {{pid}}`

- Stop profiling and print results:

`asprof stop {{pid}}`

- Profile allocations in the Java heap:

`asprof -e alloc -d 30 -f {{path/to/alloc.html}} {{pid}}`

- Profile lock contention:

`asprof -e lock -d 30 -f {{path/to/locks.html}} {{pid}}`

- Profile a single Java process found by `jps`:

`asprof -d 30 jps`

- Dump results as a collapsed stack format:

`asprof -d 30 -o collapsed -f {{path/to/profile.txt}} {{pid}}`
