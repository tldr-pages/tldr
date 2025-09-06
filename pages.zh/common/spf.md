# spf

> superfile – 现代终端文件管理器。
> 更多信息：<https://github.com/yorukot/superfile>.

- 使用指定路径启动 `spf`：

`spf {{path/to/directory}}`

- 使用多个路径启动 `spf`：

`spf {{path/to/directory1 path/to/directory2 ...}}`

- 修复快捷键设置，补全缺失的按键：

`spf {{[--fh|--fix-hotkeys]}}`

- 修复配置文件，补全缺失的项：

`spf {{[--fch|--fix-config-file]}}`

- 使用指定的配置文件与快捷键文件：

`spf {{[-c|--config-file]}} {{path/to/config.toml}} {{[--hf|--hotkey-file]}} {{path/to/hotkey.toml}}`

- 将第一个选中的文件路径写入该文件并退出：

`spf {{[--cf|--chooser-file]}} {{tmp/chooser-result}}`

- 显示内部配置和数据目录路径：

`spf {{[pl|path-list]}}`
