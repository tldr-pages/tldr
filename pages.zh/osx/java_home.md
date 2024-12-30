# java_home

> 返回 $JAVA_HOME 的值或使用该变量执行命令。
> 更多信息：<https://www.unix.com/man-page/osx/1/java_home>。

- 列出基于特定版本的 JVM：

`java_home --version {{1.5+}}`

- 列出基于特定架构的 JVM：

`java_home --arch {{i386}}`

- 列出基于特定任务的 JVM（默认值为 `CommandLine`）：

`java_home --datamodel {{Applets|WebStart|BundledApp|JNI|CommandLine}}`

- 以 XML 格式列出 JVM：

`java_home --xml`

- 显示帮助信息：

`java_home --help`