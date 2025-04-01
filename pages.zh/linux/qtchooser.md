# qtchooser

> 用于在 Qt 开发二进制版本之间进行选择的包装器。
> 更多信息：<https://manned.org/qtchooser>.

- 列出配置文件中的可用 Qt 版本：

`qtchooser --list-versions`

- 打印环境信息：

`qtchooser --print-env`

- 使用指定的 Qt 版本运行指定的工具：

`qtchooser --run-tool={{tool}} --qt={{version_name}}`

- 添加一个 Qt 版本条目以便选择：

`qtchooser --install {{version_name}} {{path/to/qmake}}`

- 显示帮助：

`qtchooser --help`