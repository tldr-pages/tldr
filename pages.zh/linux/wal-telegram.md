# wal-telegram

> 基于 pywal/wal 生成的颜色为 Telegram 生成主题。
> 更多信息：<https://github.com/guillaumeboehm/wal-telegram>.

- 使用 wal 的调色板和当前壁纸（仅限 feh）生成主题：

`wal-telegram`

- 使用 wal 的调色板和指定的背景图像生成主题：

`wal-telegram --background={{path/to/image}}`

- 使用 wal 的调色板和基于调色板的彩色背景生成主题：

`wal-telegram --tiled`

- 对背景图像应用高斯模糊：

`wal-telegram -g`

- 指定生成主题的保存位置（默认是 `$XDG_CACHE_HOME/wal-telegram` 或 `~/.cache/wal-telegram`）：

`wal-telegram --destination={{path/to/destination}}`

- 在生成主题后重新启动 Telegram 应用：

`wal-telegram --restart`