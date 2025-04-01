# f3write

> 通过填充 .h2w 文件来测试存储设备的实际容量。
> 参见: `f3read`, `f3probe`, `f3fix`。
> 更多信息：<https://oss.digirati.com.br/f3/>。

- 将测试文件写入指定目录，填满存储设备：

`f3write {{path/to/mount_point}}`

- 限制写入速度：

`f3write --max-write-rate={{kb_per_second}} {{path/to/mount_point}}`