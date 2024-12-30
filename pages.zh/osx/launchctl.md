# launchctl

> 控制苹果的 `launchd` 管理器，用于启动守护进程（系统范围的服务）和启动代理（每个用户的程序）。
> `launchd` 加载位于适当位置的基于 XML 的 `*.plist` 文件，并根据其定义的计划运行相应的命令。
> 更多信息：<https://keith.github.io/xcode-man-pages/launchctl.1.html>。

- 激活一个用户特定的代理，在用户登录时加载到 `launchd`：

`launchctl load ~/Library/LaunchAgents/{{my_script}}.plist`

- 激活一个需要以 root 权限运行的代理，和/或在任何用户登录时加载（注意路径中没有 `~`）：

`sudo launchctl load /Library/LaunchAgents/{{root_script}}.plist`

- 激活一个系统范围的守护进程，在系统启动时加载（即使没有用户登录）：

`sudo launchctl load /Library/LaunchDaemons/{{system_daemon}}.plist`

- 显示所有已加载的代理/守护进程，如果它们指定的进程当前正在运行，则显示 PID，以及它们上次运行时返回的退出代码：

`launchctl list`

- 卸载当前已加载的代理，例如以进行更改（注意：plist 文件在重启和/或登录后会自动加载到 `launchd` 中）：

`launchctl unload ~/Library/LaunchAgents/{{my_script}}.plist`

- 手动运行一个已知的（已加载的）代理/守护进程，即使此时并不合适（注意：此命令使用代理的标签，而不是文件名）：

`launchctl start {{script_file}}`

- 手动终止与已知代理/守护进程相关联的进程，如果它正在运行：

`launchctl stop {{script_file}}`