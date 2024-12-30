# lsyncd

> 监视文件和目录，并在其更改时运行 `rsync`。
> 它通常用于保持两个不同系统上的目录同步，确保在一个目录中所做的更改立即反映到另一个目录中。
> 更多信息：<https://github.com/lsyncd/lsyncd>。

- 监视源目录的更改，并在每次更改时运行 `rsync` 将文件同步到目标：

`lsyncd -rsync {{path/to/source}} {{host::share_name}}`

- 使用 SSH 而不是 `rsyncd` 共享：

`lsyncd -rsyncssh {{path/to/source}} {{host}} {{path/to/destination}}`