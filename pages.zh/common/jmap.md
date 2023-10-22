# jmap

> Java 内存映射工具。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/jmap.html>.

- 打印 Java 进程的共享对象映射（类似 pmap 的输出）：

`jmap {{Java 进程号}}`

- 打印堆摘要信息：

`jmap -heap {{Java 进程号}}`

- 按类型打印堆使用的直方图：

`jmap -histo {{Java 进程号}}`

- 将堆的内容转储到二进制文件中以使用 jhat 进行分析：

`jmap -dump:format=b,file={{导出文件名}} {{Java 进程号}}`
