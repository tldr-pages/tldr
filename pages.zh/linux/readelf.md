# readelf

> 显示EFI文件信息.
> 更多信息: <http://man7.org/linux/man-pages/man1/readelf.1.html>.

- 显示ELF所有文件信息:

`readelf -all {{path/to/binary}}`

- 显示ELF文件的所有头信息:

`readelf --headers {{path/to/binary}}`

- 如果存在符号表项，则显示ELF文件内的符号表项:

`readelf --symbols {{path/to/binary}}`

- 显示ELF文件头信息:

`readelf --file-header {{path/to/binary}}`
