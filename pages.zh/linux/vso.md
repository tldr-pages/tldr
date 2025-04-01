# vso

> Vanilla OS 的软件包管理器、系统更新器和任务自动化工具。
> 更多信息：<https://github.com/Vanilla-OS/vanilla-system-operator>。

- 检查主机系统的更新：

`vso sys-upgrade check`

- 立即升级主机系统：

`vso sys-upgrade upgrade --now`

- 初始化 Pico 子系统（用于包管理）：

`vso pico-init`

- 在子系统中安装应用程序：

`vso install {{package1 package2 ...}}`

- 从子系统中卸载应用程序：

`vso remove {{package1 package2 ...}}`

- 进入子系统的 shell：

`vso shell`

- 从子系统运行应用程序：

`vso run {{package}}`

- 显示 VSO 配置：

`vso config show`
