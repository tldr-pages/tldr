# 7za

> 具有高压缩比的文件存档程序
> `7z` 的独立版本，支持较少的存档类型
> 主页：<https://www.7-zip.org/>

- 压缩文件或目录:

`7za a {{archived.7z}} {{path/to/file_or_directory}}`

- 按原始目录结构提取一个现有的 7z 文件:

`7za x {{archived}}`

- 使用特定的压缩类型进行压缩存档:

`7za a -t{{zip|gzip|bzip2|tar}} {{archived}} {{path/to/file_or_directory}}`

- 列出可用的压缩存档类型:

`7za i`

- 列出压缩文件的内容:

`7za l {{archived}}`

