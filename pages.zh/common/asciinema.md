# asciinema

> 录制和回放终端会话，并可选分享到 <https://asciinema.org>。
> 另见：`terminalizer`。
> 更多信息：<https://docs.asciinema.org/manual/cli/usage>.

- 将本地安装的 `asciinema` 与 asciinema.org 账号关联：

`asciinema auth`

- 新建录制并保存到本地文件（按 `<Ctrl d>` 或输入 `exit` 结束）：

`asciinema rec {{路径/到/录制文件.cast}}`

- 从本地文件回放终端录制：

`asciinema play {{路径/到/录制文件.cast}}`

- 回放托管在 <https://asciinema.org> 的终端录制：

`asciinema play https://asciinema.org/a/{{文件 ID}}`

- 新建录制，限制空闲时间最多 2.5 秒：

`asciinema rec {{[-i|--idle-time-limit]}} 2.5`

- 打印本地保存录制的完整输出：

`asciinema cat {{路径/到/录制文件.cast}}`

- 上传本地保存的终端录制到 asciinema.org：

`asciinema upload {{路径/到/录制文件.cast}}`
