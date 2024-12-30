# fadvise

> 控制 Linux 文件缓存行为。
> 更多信息：<https://manned.org/fadvise>。

- 将文件预加载到缓存中：

`fadvise {{-a|--advice}} willneed {{path/to/file}}`

- 建议将文件从缓存中删除：

`fadvise {{path/to/file}}`

- 显示帮助信息：

`fadvise --help`