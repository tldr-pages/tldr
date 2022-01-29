# java

> Java 程序启动器。
> 更多信息：<https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html>.

- 通过提供类名称运行一个含有 main 函数的 java .class 程序：

`java {{类名称}}`

- 运行一个 .jar 程序：

`java -jar {{文件名.jar}}`

- 运行一个 .jar 程序并且在端口 5005 等待调试器：

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{文件名.jar}}`

- 显示 JDK, JRE 和 HotSpot 的版本：

`java -version`

- 显示详细的帮助：

`java -help`
