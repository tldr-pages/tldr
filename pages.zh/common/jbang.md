# jbang

> 简便地创建、编辑和运行仅包含源代码的自包含 Java 程序。
> 此命令也有关于其子命令的文件，例如：`java`.
> 更多信息：<https://www.jbang.dev/documentation/jbang/latest/cli/jbang.html>.

- 初始化一个简单的 Java 类：

`jbang init {{路径/到/文件.java}}`

- 初始化一个 Java 类（用于脚本编写）：

`jbang init --template={{cli}} {{路径/到/文件.java}}`

- 使用 `jshell` 在 REPL 编辑器中探索和使用脚本及其任何依赖项：

`jbang run --interactive`

- 设置一个临时项目以在 IDE 中编辑脚本：

`jbang edit --open={{codium|code|eclipse|idea|netbeans|gitpod}} {{路径/到/脚本.java}}`

- 运行 Java 代码片段（Java 9 及以后版本）：

`{{echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'}} | jbang -`

- 运行命令行应用程序：

`jbang {{路径/到/文件.java}} {{命令}} {{参数1 参数2 ...}}`

- 在用户的 `$PATH` 中安装一个脚本：

`jbang app install --name {{命令名称}} {{路径/到/脚本.java}}`

- 安装一个特定版本的 JDK 以与 `jbang` 一起使用：

`jbang jdk install {{版本}}`
