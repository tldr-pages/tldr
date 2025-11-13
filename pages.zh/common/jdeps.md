# jdeps

> Java 类依赖分析器。
> 更多信息：<https://docs.oracle.com/en/java/javase/25/docs/specs/man/jdeps.html>.

- 分析 `.jar` 或 `.class` 文件的依赖关系：

`jdeps {{路径/到/文件名.class}}`

- 打印特定 `.jar` 文件的所有依赖关系摘要：

`jdeps {{路径/到/文件名.jar}} -summary`

- 打印 `.jar` 文件的所有类级依赖关系：

`jdeps {{路径/到/文件名.jar}} -verbose`

- 将分析结果输出为 DOT 文件到指定目录：

`jdeps {{路径/到/文件名.jar}} -dotoutput {{路径/到/目录}}`

- 显示帮助信息：

`jdeps --help`
