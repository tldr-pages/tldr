# deluge-console

> Deluge BitTorrent 客户端的交互式界面。
> 更多信息：<https://deluge-torrent.org>。

- 启动交互式控制台界面：

`deluge-console`

- 连接到 Deluge 守护进程实例：

`connect {{hostname}}:{{port}}`

- 向守护进程添加种子：

`add {{url|magnet|path/to/file}}`

- 显示所有种子的信息：

`info`

- 显示特定种子的信息：

`info {{torrent_id}}`

- 暂停种子：

`pause {{torrent_id}}`

- 恢复种子：

`resume {{torrent_id}}`

- 从守护进程中删除种子：

`rm {{torrent_id}}`
