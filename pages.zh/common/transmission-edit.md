# transmission-edit

> 修改种子文件中的公告网址。
> 另见：`transmission`。
> 更多信息：<https://manned.org/transmission-edit>。

- 从种子的公告列表中添加或删除网址：

`transmission-edit --{{add|delete}} {{http://example.com}} {{path/to/file.torrent}}`

- 更新种子文件中跟踪器的密码：

`transmission-edit --replace {{old-passcode}} {{new-passcode}} {{path/to/file.torrent}}`