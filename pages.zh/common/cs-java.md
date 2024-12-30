# cs java

> `java` 和 `java-home` 命令用于获取和安装 JVM。`java` 命令也可以运行它们。
> 更多信息：<https://get-coursier.io/docs/cli-java>。

- 使用 coursier 显示 Java 版本：

`cs java -version`

- 使用 coursier 调用具有自定义属性的特定 Java 版本：

`cs java --jvm {{jvm_name}}:{{jvm_version}} -Xmx32m -X{{another_jvm_opt}} -jar {{path/to/jar_name.jar}}`

- 列出 coursier 默认索引中所有可用的 JVM：

`cs java --available`

- 列出系统中所有已安装的 JVM 及其位置：

`cs java --installed`

- 将特定 JVM 设置为当前 shell 实例的一次性默认值：

`cs java --jvm {{jvm_name}}:{{jvm_version}} --env`

- 撤销默认 JVM 设置的更改：

`eval "$(cs java --disable)"`

- 将特定 JVM 设置为整个系统的默认值：

`cs java --jvm {{jvm_name}}:{{jvm_version}} --setup`