# spf

> superfile – 现代终端文件管理器。
> 更多信息：<https://github.com/yorukot/superfile>.

- 使用指定路径启动 `spf`：

`spf {{/path/to/start}}`

- 使用多个路径启动 `spf`：

`spf {{/path/to/start1}} {{/path/to/start2}}`

- 修复快捷键设置，补全缺失的按键：

`spf --fix-hotkeys`

- 修复配置文件，补全缺失的项：

`spf --fix-config-file`

- 使用指定的配置文件与快捷键文件：

`spf --config-file {{path/to/config.toml}} --hotkey-file {{path/to/hotkey.toml}}`

- 设置选择器文件：将打开的路径写入该文件并退出：

`spf --chooser-file {{/tmp/chooser-result}}`

- 显示内部配置和数据目录路径：

`spf path-list`
