# gsettings

> 查询和修改 dconf 设置，并进行模式验证。
> 更多信息：<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>。

- 设置一个键的值。如果该键不存在或值超出范围，则会失败：

`gsettings set {{org.example.schema}} {{example-key}} {{value}}`

- 打印一个键的值，如果该键未在 `dconf` 中设置，则打印模式提供的默认值：

`gsettings get {{org.example.schema}} {{example-key}}`

- 取消设置一个键，这样将使用其模式默认值：

`gsettings reset {{org.example.schema}} {{example-key}}`

- 显示所有（不可重定位）模式、键和值：

`gsettings list-recursively`

- 从一个模式中显示所有键和值（如果未设置则为默认值）：

`gsettings list-recursively {{org.example.schema}}`

- 显示一个键的模式允许的值（对枚举键有帮助）：

`gsettings range {{org.example.schema}} {{example-key}}`

- 显示一个键的可读描述：

`gsettings describe {{org.example.schema}} {{example-key}}`