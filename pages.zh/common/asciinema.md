# asciinema

> 录制和重放终端会话，并可以选择将其分享在 <https://asciinema.org> 上。
> 请参阅：`terminalizer`。
> 更多信息：<https://docs.asciinema.org/manual/cli/usage>.

- 将本地安装的`asciinema`与 asciinema.org 账号关联：

`asciinema auth`

- 进行新的录制（使用 `<Ctrl d>` 完成录制或键入 `exit`，然后选择上传或保存到本地）：

`asciinema rec`

- 进行新的录制，保存到本地的文件中：

`asciinema rec {{路径/到/录制文件.cast}}`

- 从本地文件中播放终端录屏：

`asciinema play {{路径/到/录制文件.cast}}`

- 在 <https://asciinema.org> 中播放终端录屏：

`asciinema play https://asciinema.org/a/{{文件 ID}}`

- 进行新的录制，将闲置时间设置为最多 2.5 秒：

`asciinema rec {{[-i|--idle-time-limit]}} 2.5`

- 打印本地保存的录像的完整输出：

`asciinema cat {{路径/到/录制文件.cast}}`

- 从本地上传一个录屏到 asciinema.org：

`asciinema upload {{路径/到/录制文件.cast}}`
