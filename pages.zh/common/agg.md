# agg

> 从 `asciinema` 终端会话录制创建一个 GIF。
> 更多信息：<https://docs.asciinema.org/manual/agg/usage/>.

- 创建一个 GIF：

`agg {{路径/到/演示.cast}} {{路径/到/演示.gif}}`

- 创建一个宽度为 80 列、高度为 25 行的 GIF：

`agg --cols 80 --rows 25 {{路径/到/演示.cast}} {{路径/到/演示.gif}}`

- 创建一个字体大小为 24 像素的 GIF：

`agg --font-size 24 {{路径/到/演示.cast}} {{路径/到/演示.gif}}`

- 显示帮助：

`agg {{[-h|--help]}}`
