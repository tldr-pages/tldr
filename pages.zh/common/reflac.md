# reflac

> 重新压缩 FLAC 文件，同时保留元数据。
> 更多信息：<https://github.com/chungy/reflac>.

- 重新压缩一个目录中的 FLAC 文件：

`reflac {{path/to/directory}}`

- 启用最大压缩（非常慢）：

`reflac --best {{path/to/directory}}`

- 显示处理中的文件名：

`reflac --verbose {{path/to/directory}}`

- 递归处理子目录：

`reflac --recursive {{path/to/directory}}`

- 保留文件修改时间：

`reflac --preserve {{path/to/directory}}`
