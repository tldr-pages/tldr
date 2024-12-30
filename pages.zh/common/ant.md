# Ant

> Apache Ant：构建和管理基于Java的项目。
> 更多信息：<https://ant.apache.org>。

- 使用默认构建文件 `build.xml` 构建项目：

`ant`

- 使用其他构建文件 [f]ile 而非 `build.xml` 构建项目：

`ant -f {{buildfile.xml}}`

- 打印该项目可能的目标信息：

`ant -p`

- 打印调试信息：

`ant -d`

- 执行所有不依赖于失败目标的目标：

`ant -k`