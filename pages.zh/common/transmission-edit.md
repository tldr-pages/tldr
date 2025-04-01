# transmission-edit

> 修改 torrent 文件中的公告 URL。
> 参见：`transmission`。
> 更多信息： <https://manned.org/transmission-edit>。

- 向 torrent 的公告列表中添加或删除一个 URL：

`transmission-edit --{{add|delete}} {{http://example.com}} {{path/to/file.torrent}}`

- 更新 torrent 文件中的跟踪器密码：

`transmission-edit --replace {{old-passcode}} {{new-passcode}} {{path/to/file.torrent}}`