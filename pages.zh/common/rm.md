# rm

> 删除文件或目录。
> 另见：`rmdir`。
> 更多信息：<https://www.gnu.org/software/coreutils/rm>。

- 删除特定文件：

`rm {{path/to/file1 path/to/file2 ...}}`

- 删除特定文件，忽略不存在的文件：

`rm -f {{path/to/file1 path/to/file2 ...}}`

- 交互式删除特定文件，在每次删除前提示：

`rm -i {{path/to/file1 path/to/file2 ...}}`

- 删除特定文件并打印每次删除的信息：

`rm -v {{path/to/file1 path/to/file2 ...}}`

- 递归删除特定文件和目录：

`rm -r {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`