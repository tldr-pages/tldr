# fclones

> 高效的重复文件查找和删除工具。
> 更多信息：<https://github.com/pkolaczk/fclones>。

- 在当前目录中搜索重复文件：

`fclones group .`

- 在多个目录中搜索重复文件并缓存结果：

`fclones group --cache {{path/to/directory1 path/to/directory2}}`

- 仅在指定目录中搜索重复文件，跳过子目录，并将结果保存到文件中：

`fclones group {{path/to/directory}} --depth 1 > {{path/to/file.txt}}`

- 将 TXT 文件中的重复文件移动到不同的目录：

`fclones move {{path/to/target_directory}} < {{path/to/file.txt}}`

- 对 TXT 文件中的软链接进行干运行，而不实际创建链接：

`fclones link --soft < {{path/to/file.txt}} --dry-run 2 > /dev/null`

- 从当前目录中删除最新的重复文件，而不将它们存储在文件中：

`fclones group . | fclones remove --priority newest`

- 通过使用外部命令在匹配重复文件之前去除当前目录中 JPEG 文件的 EXIF 数据进行预处理：

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`