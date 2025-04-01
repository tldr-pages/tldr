# mandb

> 管理预格式化的手册页数据库。
> 更多信息：<https://manned.org/mandb>.

- 清除并处理手册页：

`mandb`

- 更新单个条目：

`mandb --filename {{path/to/file}}`

- 从头创建条目而不是更新：

`mandb --create`

- 仅处理用户数据库：

`mandb --user-db`

- 不清除过期的条目：

`mandb --no-purge`

- 检查手册页的有效性：

`mandb --test`