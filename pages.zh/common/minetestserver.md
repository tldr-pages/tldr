# minetestserver

> 多人在线无限世界方块沙盒服务器。
> 另见 `minetest`，图形客户端。
> 更多信息：<https://wiki.minetest.org/Setting_up_a_server>。

- 启动服务器：

`minetestserver`

- 列出可用的世界：

`minetestserver --world list`

- 加载指定的世界：

`minetestserver --world {{world_name}}`

- 列出可用的游戏 ID：

`minetestserver --gameid list`

- 使用指定的游戏：

`minetestserver --gameid {{game_id}}`

- 在特定端口上监听：

`minetestserver --port {{34567}}`

- 迁移到不同的数据后端：

`minetestserver --migrate {{sqlite3|leveldb|redis}}`

- 启动服务器后进入交互式终端：

`minetestserver --terminal`