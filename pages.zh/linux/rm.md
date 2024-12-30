# rm

> 删除文件或目录。
> 另请参阅：`rmdir`。
> 更多信息：<https://www.gnu.org/software/coreutils/rm>。

- 删除特定文件：

`rm {{path/to/file1 path/to/file2 ...}}`

- 删除特定文件并忽略不存在的文件：

`rm --force {{path/to/file1 path/to/file2 ...}}`

- 交互式删除特定文件，在每次删除之前提示确认：

`rm --interactive {{path/to/file1 path/to/file2 ...}}`

- 删除特定文件并打印每次删除的信息：

`rm --verbose {{path/to/file1 path/to/file2 ...}}`

- 递归删除特定文件和目录：

`rm --recursive {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 删除空目录（这被认为是安全的方法）：

`rm --dir {{path/to/directory}}`