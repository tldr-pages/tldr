# nextflow

> 运行计算管道。主要用于生物信息学工作流。
> 更多信息：<https://www.nextflow.io>。

- 运行管道，使用之前运行的缓存结果：

`nextflow run {{main.nf}} -resume`

- 从 GitHub 运行远程工作流的特定版本：

`nextflow run {{user/repo}} -revision {{release_tag}}`

- 使用给定的工作目录保存中间文件，保存执行报告：

`nextflow run {{workflow}} -work-dir {{path/to/directory}} -with-report {{report.html}}`

- 显示当前目录中之前运行的详细信息：

`nextflow log`

- 删除特定运行的缓存和中间文件：

`nextflow clean -force {{run_name}}`

- 列出所有已下载的项目：

`nextflow list`

- 从 Bitbucket 拉取远程工作流的最新版本：

`nextflow pull {{user/repo}} -hub bitbucket`

- 更新 Nextflow：

`nextflow self-update`