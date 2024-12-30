# lvremove

> 删除逻辑卷。
> 另请参见：`lvm`。
> 更多信息：<https://manned.org/lvremove>。

- 删除卷组中的逻辑卷：

`sudo lvremove {{volume_group}}/{{logical_volume}}`

- 删除卷组中的所有逻辑卷：

`sudo lvremove {{volume_group}}`