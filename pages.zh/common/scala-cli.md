# scala-cli

> 与Scala编程语言进行交互。
> 更多信息：<https://scala-cli.virtuslab.org/docs/overview/>.

- 使用特定的Scala和JVM版本启动REPL（交互式终端）：

`scala-cli --scala {{3.1.0}} --jvm {{temurin:17}}`

- 编译并运行一个Scala脚本：

`scala-cli run {{path/to/script.scala}}`

- 编译并测试一个Scala脚本：

`scala-cli test {{path/to/script.scala}}`

- 格式化一个Scala脚本，并就地更新文件：

`scala-cli fmt {{path/to/script.scala}}`

- 生成IDE（VSCode和IntelliJ）支持的文件：

`scala-cli setup-ide {{path/to/script.scala}}`