# jstack

> Java Stack Trace Tool.
> More information: <https://www.unix.com/man-page/mojave/1/jstack/>.

- Print Java stack traces for all threads in a Java process:

`jstack {{java_pid}}`

- Print mixed mode (Java/C++) stack traces for all threads in a Java process:

`jstack -m {{java_pid}}`

- Print stack traces from Java core dump:

`jstack {{/usr/bin/java}} {{file.core}}`
