# jstack

> Java 栈跟踪工具。
> 更多信息：<https://manned.org/jstack>.

- 打印 Java 进程中所有线程的 Java 栈跟踪：

`jstack {{java_进程号}}`

- 打印混合模式（Java/C++）的栈跟踪：

`jstack -m {{java_进程号}}`

- 打印来自 Java 核心转储的栈跟踪：

`jstack {{/usr/bin/java}} {{文件.core}}`
