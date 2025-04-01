# scala-cli

> 与 Scala 编程语言进行交互。
> 更多信息：<https://scala-cli.virtuslab.org/docs/overview/>.

- 使用特定的 Scala 和 JVM 版本启动 REPL（交互式 shell）：

`scala-cli --scala {{3.1.0}} --jvm {{temurin:17}}`

- 编译并运行 Scala 脚本：

`scala-cli run {{path/to/script.scala}}`

- 编译并测试 Scala 脚本：

`scala-cli test {{path/to/script.scala}}`

- 格式化 Scala 脚本，直接更新文件内容：

`scala-cli fmt {{path/to/script.scala}}`

- 生成支持 IDE（VSCode 和 IntelliJ）的文件：

`scala-cli setup-ide {{path/to/script.scala}}`