# asciinema

> 记录并重放终端会话，并可选择将其分享至 <https://asciinema.org>。
> 另见：`terminalizer`。
> 更多信息：<https://docs.asciinema.org/manual/cli/usage>。

- 将本地安装的 `asciinema` 与 asciinema.org 帐户关联：

`asciinema auth`

- 进行新的录制（用 `Ctrl+D` 完成或输入 `exit`，然后选择上传或本地保存）：

`asciinema rec`

- 进行新的录制并保存到本地文件：

`asciinema rec {{path/to/recording.cast}}`

- 从本地文件重放终端录制：

`asciinema play {{path/to/recording.cast}}`

- 重放托管在 <https://asciinema.org> 的终端录制：

`asciinema play https://asciinema.org/a/{{cast_id}}`

- 进行新的录制，将任何空闲时间限制在最多 2.5 秒：

`asciinema rec {{-i|--idle-time-limit}} 2.5`

- 打印本地保存的录制的完整输出：

`asciinema cat {{path/to/recording.cast}}`

- 将本地保存的终端会话上传至 asciinema.org：

`asciinema upload {{path/to/recording.cast}}`