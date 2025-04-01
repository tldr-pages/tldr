# termusic

> 一个用 Rust 编写的终端音乐播放器，使用类似 vim 的键绑定。
> 参见：`cmus`, `ncmpcpp`, `audacious`。
> 更多信息：<https://github.com/tramhao/termusic>。

- 打开 termusic 到指定目录。（可以在 `~/.config/termusic/config.toml` 中永久设置）：

`termusic {{path/to/directory}}`

- 禁用显示某个文件的专辑封面：

`termusic -c {{path/to/music_file}}`

- 显示帮助信息：

`termusic --help`