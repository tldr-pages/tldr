# jstack

> Java stack trace tool.
> More information: <https://manned.org/jstack>.

- Print Java stack traces for all threads in a Java process:

`jstack {{java_pid}}`

- Print mixed mode (Java/C++) stack traces for all threads in a Java process:

`jstack -m {{java_pid}}`

- Print stack traces from Java core dump:

`jstack {{/usr/bin/java}} {{file.core}}`
