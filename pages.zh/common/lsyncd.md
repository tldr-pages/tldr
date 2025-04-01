# lsyncd

> 监视文件和目录的变化，并在文件变化时运行 `rsync` 进行同步。
> 它通常用于保持两个不同系统上的目录同步，确保一个目录中的更改会立即反映到另一个目录中。
> 更多信息：<https://github.com/lsyncd/lsyncd>.

- 监视源目录的变化，并在每次变化时运行 `rsync` 将文件同步到目标目录：

`lsyncd -rsync {{path/to/source}} {{host::share_name}}`

- 使用 SSH 而不是 `rsyncd` 共享：

`lsyncd -rsyncssh {{path/to/source}} {{host}} {{path/to/destination}}`
