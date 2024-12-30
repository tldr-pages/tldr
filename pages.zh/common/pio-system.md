# pio 系统

> PlatformIO 的杂项系统命令。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/system/>.

- 为当前 shell 安装命令补全（支持 Bash、fish、Zsh 和 PowerShell）：

`pio system completion install`

- 卸载当前 shell 的命令补全：

`pio system completion uninstall`

- 显示系统范围内的 PlatformIO 信息：

`pio system info`

- 移除未使用的 PlatformIO 数据：

`pio system prune`

- 仅移除缓存数据：

`pio system prune --cache`

- 列出将被移除但实际上不移除的未使用 PlatformIO 数据：

`pio system prune --dry-run`