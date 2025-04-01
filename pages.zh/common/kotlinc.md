# kotlinc

> Kotlin 编译器。
> 更多信息：<https://kotlinlang.org/docs/command-line.html>.

- 启动 REPL（交互式 shell）:

`kotlinc`

- 编译 Kotlin 文件:

`kotlinc {{path/to/file.kt}}`

- 编译多个 Kotlin 文件:

`kotlinc {{path/to/file1.kt path/to/file2.kt ...}}`

- 执行特定的 Kotlin 脚本文件:

`kotlinc -script {{path/to/file.kts}}`

- 将 Kotlin 文件编译为包含 Kotlin 运行时库的独立 jar 文件:

`kotlinc {{path/to/file.kt}} -include-runtime -d {{path/to/file.jar}}`
