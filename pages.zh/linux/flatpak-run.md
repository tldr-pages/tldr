# flatpak run

> 运行 Flatpak 应用程序和运行时。
> 更多信息：<https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- 运行已安装的应用程序：

`flatpak run {{com.example.app}}`

- 从特定分支（例如：stable, beta, master）运行已安装的应用程序：

`flatpak run --branch={{stable|beta|master|...}} {{com.example.app}}`

- 在 Flatpak 内部运行交互式 shell：

`flatpak run --command={{sh}} {{com.example.app}}`

- 使用特定运行时版本运行已安装的应用程序：

`flatpak run --runtime-version={{24.08|master|stable|...}} {{com.example.app}}`

- 使用不同的运行时（但版本号相同）运行已安装的应用程序：

`flatpak run --runtime={{org.freedesktop.Sdk}} {{com.example.app}}`