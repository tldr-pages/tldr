# ncmpcpp

> 音乐播放器守护进程的客户端。
> 详见: `mpd`, `mpc`, `qmmp`, `termusic`。
> 更多信息: <https://rybczak.net/ncmpcpp>。

- 连接到指定主机和端口上的音乐播放器守护进程：

`ncmpcpp --host {{ip}} --port {{port}}`

- 在控制台显示当前歌曲的元数据：

`ncmpcpp --current-song`

- 使用指定的配置文件：

`ncmpcpp --config {{file}}`

- 使用来自文件的不同键绑定集：

`ncmpcpp --bindings {{file}}`