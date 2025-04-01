# gsettings

> 查询和修改带有模式验证的 dconf 设置。
> 更多信息：<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>.

- 设置键的值。如果键不存在或值超出范围则会失败：

`gsettings set {{org.example.schema}} {{example-key}} {{value}}`

- 打印键的值，如果在 `dconf` 中未设置该键，则打印模式提供的默认值：

`gsettings get {{org.example.schema}} {{example-key}}`

- 重置键，使其使用模式的默认值：

`gsettings reset {{org.example.schema}} {{example-key}}`

- 显示所有（不可重定位的）模式、键和值：

`gsettings list-recursively`

- 显示某一模式下的所有键和值（未设置的使用默认值）：

`gsettings list-recursively {{org.example.schema}}`

- 显示键的模式允许值（对于枚举键特别有帮助）：

`gsettings range {{org.example.schema}} {{example-key}}`

- 显示键的可读描述：

`gsettings describe {{org.example.schema}} {{example-key}}`