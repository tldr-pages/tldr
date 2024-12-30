# pvremove

> 从物理卷中移除 LVM 标签。
> 更多信息：<https://manned.org/pvremove>。

- 从物理卷中移除 LVM 标签：

`sudo pvremove {{/dev/sdXY}}`

- 在操作过程中显示详细输出：

`sudo pvremove --verbose {{/dev/sdXY}}`

- 在不询问确认的情况下移除 LVM 标签：

`sudo pvremove --yes {{/dev/sdXY}}`

- 强制移除 LVM 标签：

`sudo pvremove --force {{/dev/sdXY}}`

- 以 JSON 格式显示输出：

`sudo pvremove --reportformat json {{/dev/sdXY}}`