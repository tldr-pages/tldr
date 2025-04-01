# cs fetch

> cs fetch 用于下载依赖的 JAR 文件。
> 更多信息：<https://get-coursier.io/docs/cli-fetch>.

- 下载特定版本的 JAR 文件：

`cs fetch {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 下载包，并评估与所选包对应类路径的环境变量：

`CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"`

- 下载特定 JAR 文件的源代码：

`cs fetch --sources {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 下载 JAR 文件的 Java 文档：

`cs fetch --javadoc {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 下载带有 Java 文档和源代码的依赖项：

`cs fetch --default={{true}} --sources --javadoc {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 从依赖文件下载 JAR 文件：

`cs fetch {{--dependency-file path/to/file1 --dependency-file path/to/file2 ...}}`