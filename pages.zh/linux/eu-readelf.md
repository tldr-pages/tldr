# eu-readelf

> 显示 ELF 文件的信息。
> 更多信息：<https://manned.org/eu-readelf>.

- 显示 ELF 文件中所有可提取的信息：

`eu-readelf {{[-a|--all]}} {{path/to/file}}`

- 显示所有 NOTE 段/节的内容，或特定段/节的内容：

`eu-readelf {{[-n--notes]}} {{.note.ABI-tag}} {{path/to/file}}`
