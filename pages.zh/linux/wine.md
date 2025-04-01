# wine

> 在基于 Unix 的系统上运行 Windows 可执行文件。
> 更多信息：<https://wiki.winehq.org/>。

- 在 `wine` 环境中运行特定程序：

`wine {{command}}`

- 在后台运行特定程序：

`wine start {{command}}`

- 安装或卸载 MSI 包：

`wine msiexec /{{i|x}} {{path/to/package.msi}}`

- 运行“文件资源管理器”、“记事本”或“写字板”：

`wine {{explorer|notepad|write}}`

- 运行“注册表编辑器”、“控制面板”或“任务管理器”：

`wine {{regedit|control|taskmgr}}`

- 运行配置工具：

`wine winecfg`
