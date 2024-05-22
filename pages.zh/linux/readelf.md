# readelf

> 显示 EFI 文件信息。
> 更多信息：<https://manned.org/readelf.1>.

- 显示 ELF 所有文件信息：

`readelf -all {{path/to/binary}}`

- 显示 ELF 文件的所有头信息：

`readelf --headers {{path/to/binary}}`

- 如果存在符号表项，则显示 ELF 文件内的符号表项：

`readelf --symbols {{path/to/binary}}`

- 显示 ELF 文件头信息：

`readelf --file-header {{path/to/binary}}`
