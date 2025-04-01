# nf-core

> nf-core 框架工具，用于创建、检查和开发 Nextflow 的最佳实践指南。
> 更多信息：<https://nf-co.re/docs/nf-core-tools>.

- 列出 nf-core 上现有的管道：

`nf-core list`

- 创建一个新的管道框架：

`nf-core create`

- 检查管道代码：

`nf-core lint {{path/to/directory}}`

- 更新管道配方中的软件版本：

`nf-core bump-version {{path/to/directory}} {{new_version}}`

- 启动一个 nf-core 管道：

`nf-core launch {{pipeline_name}}`

- 下载一个 nf-core 管道以便离线使用：

`nf-core download {{pipeline_name}}`
