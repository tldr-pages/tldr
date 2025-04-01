# bchunk

> 将 CD 镜像转换为一组 `.iso` 和 `.cdr` 轨道。
> 更多信息：<http://he.fi/bchunk>.

- 将二进制 CD 转换为标准的 iso9660 镜像文件：

`bchunk {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`

- 以详细模式转换：

`bchunk -v {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`

- 以 WAV 格式输出音频文件：

`bchunk -w {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`
