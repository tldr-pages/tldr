# softwareupdate

> 更新 macOS App Store 应用程序。
> 更多信息: <https://keith.github.io/xcode-man-pages/softwareupdate.8.html>。

- 列出所有可用的更新：

`softwareupdate --list`

- 下载并安装所有更新：

`softwareupdate --install --all`

- 下载并安装所有 [r]ecommended 更新：

`softwareupdate --install --recommended`

- 下载并安装特定应用程序：

`softwareupdate --install {{update_name}}`