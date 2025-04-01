# fadvise

> 控制 Linux 文件缓存行为。
> 更多信息：<https://manned.org/fadvise>.

- 将文件预加载到缓存中：

`fadvise {{[-a|--advice]}} willneed {{path/to/file}}`

- 建议从缓存中移除文件：

`fadvise {{path/to/file}}`

- 显示帮助：

`fadvise {{[-h|--help]}}`