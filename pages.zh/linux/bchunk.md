# bchunk

> 将 CD 镜像转换为一组 `.iso` 和 `.cdr` 音轨。
> 更多信息：<http://he.fi/bchunk>。

- 将二进制 CD 转换为标准 iso9960 镜像文件：

`bchunk {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`

- 以详细模式转换：

`bchunk -v {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`

- 输出 WAV 格式的音频文件：

`bchunk -w {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`