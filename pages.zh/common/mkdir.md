# mkdir

> 创建目录并设置其权限。
> 更多信息：<https://www.gnu.org/software/coreutils/mkdir>。

- 创建特定目录：

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- 创建特定目录及其父目录（如有必要）：

`mkdir {{-p|--parents}} {{path/to/directory1 path/to/directory2 ...}}`

- 以特定权限创建目录：

`mkdir {{-m|--mode}} {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`