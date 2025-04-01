# idea

> JetBrains 的 Java 和 Kotlin 集成开发环境。
> 更多信息：<https://www.jetbrains.com/help/idea/working-with-the-ide-features-from-command-line.html>.

- 在 IntelliJ IDEA 中打开当前目录：

`idea {{path/to/directory}}`

- 在 IntelliJ IDEA 中打开特定的文件或目录：

`idea {{path/to/file_or_directory}}`

- 打开差异查看器以比较最多 3 个文件：

`idea diff {{path/to/file1 path/to/file2 path/to/optional_file3}}`

- 打开合并对话框以执行两文件合并：

`idea merge {{path/to/file1}} {{path/to/file2}} {{path/to/output}}`

- 在项目上运行代码检查：

`idea inspect {{path/to/project_directory}} {{path/to/inspection_profile}} {{path/to/output}}`
