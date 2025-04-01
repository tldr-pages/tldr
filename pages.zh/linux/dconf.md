# dconf

> 管理 dconf 数据库。
> 参见：`dconf-read`，`dconf-reset`，`dconf-write`，`gsettings`。
> 更多信息：<https://manned.org/dconf>.

- 打印特定键的值：

`dconf read {{/path/to/key}}`

- 打印特定路径的子目录和子键：

`dconf list {{/path/to/directory/}}`

- 写入特定键的值：

`dconf write {{/path/to/key}} "{{value}}"`

- 重置特定键的值：

`dconf reset {{/path/to/key}}`

- 监视特定键或目录的更改：

`dconf watch {{/path/to/key|/path/to/directory/}}`

- 以 INI 文件格式导出特定目录：

`dconf dump {{/path/to/directory/}}`
