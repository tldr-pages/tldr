# jstack

> Java stack trace eszköz. További információ: <https://manned.org/jstack>.

- Java stack traces nyomtatása egy Java-folyamat összes szálára:

`jstack {{java_pid}}`

- Vegyes üzemmódú (Java/C++) stack traces nyomtatása egy Java-folyamat összes szálára:

`jstack -m {{java_pid}}`

- Stack traces nyomtatása Java core dumpból:

`jstack {{/usr/bin/java}} {{file.core}}`
