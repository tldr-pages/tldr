# readelf

> 显示有关 ELF 文件的信息。
> 更多信息：<https://manned.org/readelf.1>。

- 显示 ELF 文件的所有信息：

`readelf -all {{path/to/binary}}`

- 显示 ELF 文件中存在的所有头部信息：

`readelf --headers {{path/to/binary}}`

- 显示 ELF 文件符号表部分的条目（如果存在）：

`readelf --symbols {{path/to/binary}}`

- 显示 ELF 头部信息：

`readelf --file-header {{path/to/binary}}`

- 显示 ELF 部分头部信息：

`readelf --section-headers {{path/to/binary}}`