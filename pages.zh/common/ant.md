# ant

> Apache Ant。
> 用于构建和管理基于 Java 的项目的工具。
> 更多信息：<https://ant.apache.org>.

- 用默认的构建文件 `build.xml` 构建一个项目：

`ant`

- 使用 `build.xml` 以外的构建文件构建项目：

`ant -f {{构建文件.xml}}`

- 打印该项目可能的目标信息：

`ant -p`

- 打印调试信息：

`ant -d`

- 执行所有不依赖失败目标的目标：

`ant -k`
