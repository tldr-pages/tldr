# fclones

> 高效的重复文件查找和删除工具。
> 更多信息：<https://github.com/pkolaczk/fclones>.

- 在当前目录中查找重复文件：

`fclones group .`

- 在多个目录中查找重复文件并缓存结果：

`fclones group --cache {{path/to/directory1 path/to/directory2}}`

- 仅在指定目录中查找重复文件，跳过子目录并将结果保存到文件中：

`fclones group {{path/to/directory}} --depth 1 > {{path/to/file.txt}}`

- 将TXT文件中的重复文件移动到不同目录：

`fclones move {{path/to/target_directory}} < {{path/to/file.txt}}`

- 对TXT文件中的软链接执行干运行，但不实际创建链接：

`fclones link --soft < {{path/to/file.txt}} --dry-run 2 > /dev/null`

- 删除当前目录中的最新重复文件，不将它们存储在文件中：

`fclones group . | fclones remove --priority newest`

- 预处理当前目录中的JPEG文件，使用外部命令删除它们的EXIF数据，然后再查找重复文件：

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`
