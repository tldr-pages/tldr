# jdeps

> Java 类依赖分析器。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/jdeps.html>。

- 分析 `.jar` 或 `.class` 文件的依赖关系：

`jdeps {{path/to/filename.class}}`

- 打印特定 `.jar` 文件的所有依赖关系摘要：

`jdeps {{path/to/filename.jar}} -summary`

- 打印 `.jar` 文件的所有类级别依赖关系：

`jdeps {{path/to/filename.jar}} -verbose`

- 将分析结果输出为 DOT 文件到特定目录：

`jdeps {{path/to/filename.jar}} -dotoutput {{path/to/directory}}`

- 显示帮助信息：

`jdeps --help`