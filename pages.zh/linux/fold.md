# fold

> 将长行折叠以适用于固定宽度的输出设备。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/fold-invocation.html>.

- 在固定宽度处折叠行：

`fold {{[-w|--width]}} {{width}} {{path/to/file}}`

- 以字节为单位计算宽度（默认是以字符列数为单位）：

`fold {{[-b|--bytes]}} {{[-w|--width]}} {{width_in_bytes}} {{path/to/file}}`

- 在宽度限制内的最右侧空格处折行：

`fold {{[-s|--spaces]}} {{[-w|--width]}} {{width}} {{path/to/file}}`