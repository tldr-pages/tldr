# f3write

> 用 .h2w 文件填充驱动器以测试其实际容量。
> 另见：`f3read`，`f3probe`，`f3fix`。
> 更多信息：<https://oss.digirati.com.br/f3/>.

- 将测试文件写入指定目录，填满驱动器：

`f3write {{path/to/mount_point}}`

- 限制写入速度：

`f3write --max-write-rate={{kb_per_second}} {{path/to/mount_point}}`