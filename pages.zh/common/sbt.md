# sbt

> Scala 和 Java 项目的构建工具。
> 更多信息：<https://www.scala-sbt.org/1.x/docs/>。

- 启动 REPL（交互式 shell）:

`sbt`

- 从 GitHub 上托管的现有 Giter8 模板创建一个新的 Scala 项目:

`sbt new {{scala/hello-world.g8}}`

- 编译并运行所有测试:

`sbt test`

- 删除 `target` 目录中的所有生成文件:

`sbt clean`

- 编译 `src/main/scala` 和 `src/main/java` 目录中的主源代码:

`sbt compile`

- 使用指定版本的 sbt:

`sbt -sbt-version {{version}}`

- 使用特定的 jar 文件作为 sbt 启动器:

`sbt -sbt-jar {{path}}`

- 列出所有 sbt 选项:

`sbt -h`