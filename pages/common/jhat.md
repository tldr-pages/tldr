# jhat

> Java Heap Analysis Tool.
> More information: <https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html>.

- Analyze a heap dump (from `jmap`), view via HTTP on port 7000:

`jhat {{dump_file.bin}}`

- Analyze a heap dump, specifying an alternate port for the http server:

`jhat -p {{port}} {{dump_file.bin}}`

- Analyze a dump letting `jhat` use up to 8 GB RAM (2-4x dump size recommended):

`jhat -J-mx8G {{dump_file.bin}}`
