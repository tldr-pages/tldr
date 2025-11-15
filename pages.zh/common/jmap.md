# jmap

> Java 内存映射工具。
> 更多信息：<https://docs.oracle.com/en/java/javase/25/docs/specs/man/jmap.html>.

- 打印 Java 进程的共享对象映射（类似 pmap 的输出）：

`jmap {{Java 进程号}}`

- 打印堆摘要信息：

`jmap -heap {{文件名.jar}} {{Java 进程号}}`

- 按类型打印堆使用的直方图：

`jmap -histo {{Java 进程号}}`

- 将堆的内容转储到二进制文件中以使用 jhat 进行分析：

`jmap -dump:format=b,file={{路径/到/文件}} {{Java 进程号}}`

- 将堆中存活的对象转储到二进制文件中以使用 jhat 进行分析：

`jmap -dump:live,format=b,file={{路径/到/文件}} {{Java 进程号}}`
