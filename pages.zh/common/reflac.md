# reflac

> 在保留元数据的同时就地重新压缩FLAC文件。
> 更多信息：<https://github.com/chungy/reflac>。

- 重新压缩FLAC文件目录：

`reflac {{path/to/directory}}`

- 启用最大压缩（非常慢）：

`reflac --best {{path/to/directory}}`

- 在处理时显示文件名：

`reflac --verbose {{path/to/directory}}`

- 递归进入子目录：

`reflac --recursive {{path/to/directory}}`

- 保留文件修改时间：

`reflac --preserve {{path/to/directory}}`