# distrobox-export

> 从容器导出应用/服务/二进制文件到主机操作系统。另请参见：`tldr distrobox`。
> 更多信息：<https://distrobox.it/usage/distrobox-export>。

- 从容器导出应用到主机（桌面条目/图标将出现在主机系统的应用程序列表中）：

`distrobox-export --app {{package}} --extra-flags "--foreground"`

- 从容器导出二进制文件到主机：

`distrobox-export --bin {{path/to/binary}} --export-path {{path/to/binary_on_host}}`

- 从容器导出二进制文件到主机（即`$HOME/.local/bin`）：

`distrobox-export --bin {{path/to/binary}} --export-path {{path/to/export}}`

- 从容器导出服务到主机（`--sudo`将在容器内以root身份运行该服务）：

`distrobox-export --service {{package}} --extra-flags "--allow-newer-config" --sudo`

- 取消导出/删除已导出的应用：

`distrobox-export --app {{package}} --delete`