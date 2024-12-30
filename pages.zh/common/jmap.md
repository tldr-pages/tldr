# jmap

> Java 内存映射工具。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/jmap.html>。

- 打印 Java 进程的共享对象映射（输出类似于 pmap）：

`jmap {{java_pid}}`

- 打印堆的摘要信息：

`jmap -heap {{filename.jar}} {{java_pid}}`

- 打印按类型的堆使用情况的直方图：

`jmap -histo {{java_pid}}`

- 将堆的内容转储到二进制文件中，以便与 jhat 分析：

`jmap -dump:format=b,file={{path/to/file}} {{java_pid}}`

- 将堆中的活动对象转储到二进制文件中，以便与 jhat 分析：

`jmap -dump:live,format=b,file={{path/to/file}} {{java_pid}}`