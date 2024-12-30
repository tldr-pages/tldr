# ln

> 创建文件和目录的链接。
> 更多信息：<https://www.gnu.org/software/coreutils/ln>。

- 创建指向文件或目录的符号链接：

`ln -s {{/path/to/file_or_directory}} {{path/to/symlink}}`

- 重写现有的符号链接以指向不同的文件：

`ln -sf {{/path/to/new_file}} {{path/to/symlink}}`

- 创建指向文件的硬链接：

`ln {{/path/to/file}} {{path/to/hardlink}}`