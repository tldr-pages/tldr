# termusic

> 一个用 Rust 编写的终端音乐播放器，使用类似 vim 的按键绑定。
> 另见：`cmus`、`ncmpcpp`、`audacious`。
> 更多信息：<https://github.com/tramhao/termusic>。

- 打开 termusic 到特定目录。（可以在 `~/.config/termusic/config.toml` 中永久设置）：

`termusic {{path/to/directory}}`

- 禁用特定文件的专辑封面显示：

`termusic -c {{path/to/music_file}}`

- 显示帮助：

`termusic --help`