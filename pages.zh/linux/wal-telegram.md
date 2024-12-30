# wal-telegram

> 基于 pywal/wal 生成 Telegram 主题。
> 更多信息：<https://github.com/guillaumeboehm/wal-telegram>。

- 使用 wal 的调色板和当前壁纸生成（仅适用于 feh）：

`wal-telegram`

- 使用 wal 的调色板和指定的背景图片生成：

`wal-telegram --background={{path/to/image}}`

- 使用 wal 的调色板和基于调色板的彩色背景生成：

`wal-telegram --tiled`

- 对背景图片应用高斯模糊：

`wal-telegram -g`

- 指定生成主题的位置（默认是 `$XDG_CACHE_HOME/wal-telegram` 或 `~/.cache/wal-telegram`）：

`wal-telegram --destination={{path/to/destination}}`

- 生成后重启 Telegram 应用：

`wal-telegram --restart`