# jstack

> Java 堆栈跟踪工具。
> 更多信息：<https://manned.org/jstack>。

- 打印 Java 进程中所有线程的 Java 堆栈跟踪：

`jstack {{java_pid}}`

- 打印 Java 进程中所有线程的混合模式 (Java/C++) 堆栈跟踪：

`jstack -m {{java_pid}}`

- 从 Java 核心转储中打印堆栈跟踪：

`jstack {{/usr/bin/java}} {{file.core}}`