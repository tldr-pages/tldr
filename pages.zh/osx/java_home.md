# java_home

> 返回 $JAVA_HOME 的值或使用此变量执行命令。
> 更多信息：<https://www.unix.com/man-page/osx/1/java_home>.

- 根据特定版本列出 JVM：

`java_home --version {{1.5+}}`

- 根据特定架构列出 JVM：

`java_home --arch {{i386}}`

- 根据特定任务列出 JVM（默认为 `CommandLine`）：

`java_home --datamodel {{Applets|WebStart|BundledApp|JNI|CommandLine}}`

- 以 XML 格式列出 JVM：

`java_home --xml`

- 显示帮助：

`java_home --help`