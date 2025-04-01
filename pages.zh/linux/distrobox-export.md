# distrobox-export

> 将容器中的应用程序/服务/二进制文件导出到主机操作系统。参见：`tldr distrobox`。
> 更多信息：<https://distrobox.it/usage/distrobox-export>。

- 从容器中导出应用程序到主机（桌面条目/图标将显示在主机系统的应用程序列表中）：

`distrobox-export --app {{package}} --extra-flags "--foreground"`

- 从容器中导出二进制文件到主机：

`distrobox-export --bin {{path/to/binary}} --export-path {{path/to/binary_on_host}}`

- 从容器中导出二进制文件到主机（即 `$HOME/.local/bin`）：

`distrobox-export --bin {{path/to/binary}} --export-path {{path/to/export}}`

- 从容器中导出服务到主机（`--sudo` 将在容器内以 root 身份运行服务）：

`distrobox-export --service {{package}} --extra-flags "--allow-newer-config" --sudo`

- 删除已导出的应用程序：

`distrobox-export --app {{package}} --delete`