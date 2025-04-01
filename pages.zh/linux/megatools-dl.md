# megatools-dl

> 从 `mega.nz` 下载文件。
> 作为 `megatools` 套件的一部分。
> 更多信息：<https://megatools.megous.com/man/megatools-dl.html>.

- 从 `mega.nz` 链接下载文件到当前目录：

`megatools-dl {{https://mega.nz/...}}`

- 从 `mega.nz` 链接下载文件到指定目录：

`megatools-dl --path {{path/to/directory}} {{https://mega.nz/...}}`

- 交互式选择要下载的文件：

`megatools-dl --choose-files {{https://mega.nz/...}}`

- 限制下载速度（单位为 KiB/s）：

`megatools-dl --limit-speed {{speed}} {{https://mega.nz/...}}`
