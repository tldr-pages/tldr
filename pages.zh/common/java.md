# Java

> Java 应用程序启动器。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>。

- 通过仅使用类名执行包含主方法的 Java `.class` 文件：

`java {{classname}}`

- 执行 Java 程序并使用额外的第三方或用户定义的类：

`java -classpath {{path/to/classes1}}:{{path/to/classes2}}:. {{classname}}`

- 执行 `.jar` 程序：

`java -jar {{filename.jar}}`

- 执行 `.jar` 程序并在端口 5005 上等待调试连接：

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- 显示 JDK、JRE 和 HotSpot 版本：

`java -version`

- 显示帮助：

`java -help`