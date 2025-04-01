# pio system

> PlatformIO 的各种系统命令。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/system/>.

- 为当前 Shell 安装命令补全（支持 Bash、fish、Zsh 和 PowerShell）：

`pio system completion install`

- 卸载当前 Shell 的命令补全：

`pio system completion uninstall`

- 显示 PlatformIO 的系统范围信息：

`pio system info`

- 删除未使用的 PlatformIO 数据：

`pio system prune`

- 仅删除缓存数据：

`pio system prune --cache`

- 列出将被删除的未使用 PlatformIO 数据，但不实际删除：

`pio system prune --dry-run`
