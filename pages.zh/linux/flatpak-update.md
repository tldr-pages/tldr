# flatpak update

> 更新 Flatpak 应用程序和运行时。
> 更多信息：<https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-update>.

- 更新所有已安装的应用程序和运行时（使用 `-y` 自动确认所有提示）：

`flatpak update`

- 仅更新特定应用：

`flatpak update {{com.example.app}}`

- 更新/降级到特定版本（另请参见 flatpak remote-info 和 flatpak mask）：

`flatpak update --commit={{COMMIT}} {{com.example.app}}`
