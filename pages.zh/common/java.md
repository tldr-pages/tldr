# java

> Java 程序启动器.
> 更多信息: <https://java.com>.

- 通过提供类名称运行一个含有 main 函数的 java .class 程序:

`java {{classname}}`

- 运行一个 .jar 程序:

`java -jar {{filename.jar}}`

- 运行一个 .jar 程序并且在端口5005等待调试器:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- 显示 JDK, JRE 和 HotSpot 的版本:

`java -version`

- 显示详细的帮助:

`java -help`
