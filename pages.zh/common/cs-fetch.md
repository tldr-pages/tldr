# cs fetch

> Fetch 用于获取依赖的 JAR 文件。
> 更多信息：<https://get-coursier.io/docs/cli-fetch>。

- 获取特定版本的 JAR 文件：

`cs fetch {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 获取一个包，并在环境变量中评估对应于所选包的类路径：

`CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"`

- 获取特定 JAR 文件的源代码：

`cs fetch --sources {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 获取 Javadoc JAR 文件：

`cs fetch --javadoc {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 获取带有 Javadoc JAR 文件和源代码 JAR 文件的依赖项：

`cs fetch --default={{true}} --sources --javadoc {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 从依赖文件中获取 JAR 文件：

`cs fetch {{--dependency-file path/to/file1 --dependency-file path/to/file2 ...}}`