# jbang

> 轻松创建、编辑和运行自包含的源代码 Java 程序。
> 另见：`java`。
> 更多信息：<https://www.jbang.dev/documentation/guide/latest/cli/jbang.html>。

- 初始化一个简单的 Java 类：

`jbang init {{path/to/file.java}}`

- 初始化一个 Java 类（适用于脚本）：

`jbang init --template={{cli}} {{path/to/file.java}}`

- 使用 `jshell` 在 REPL 编辑器中探索和使用脚本及其依赖项：

`jbang run --interactive`

- 设置一个临时项目以在 IDE 中编辑脚本：

`jbang edit --open={{codium|code|eclipse|idea|netbeans|gitpod}} {{path/to/script.java}}`

- 运行一段 Java 代码片段（Java 9 及更高版本）：

`{{echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'}} | jbang -`

- 运行命令行应用程序：

`jbang {{path/to/file.java}} {{command}} {{arg1 arg2 ...}}`

- 将脚本安装到用户的 `$PATH` 中：

`jbang app install --name {{command_name}} {{path/to/script.java}}`

- 安装特定版本的 JDK 以供 `jbang` 使用：

`jbang jdk install {{version}}`