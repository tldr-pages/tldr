# flatpak remote-info

> 显示远程仓库中应用程序或运行时的信息。
> 更多信息：<https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-info>。

- 显示 flatpak 的信息：

`flatpak remote-info {{remote_name}} {{com.example.app}}`

- 显示远程仓库中应用程序的先前版本日志：

`flatpak remote-info --log {{remote_name}} {{com.example.app}}`

- 显示特定提交的信息，而不是最新版本的信息：

`flatpak remote-info --commit={{COMMIT}} {{remote_name}} {{com.example.app}}`
