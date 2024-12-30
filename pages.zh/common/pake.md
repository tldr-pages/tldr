# pake

> 使用 Rust/Tauri 将任何网页转变为桌面应用程序。
> 更多信息：<https://github.com/tw93/Pake>。

- 打包一个网页：

`pake {{https://www.google.com/}}`

- 使用特定窗口大小打包网页：

`pake --width {{800}} --height {{600}} {{https://www.google.com/}}`

- 使用自定义应用名称和图标打包网页：

`pake --name {{Google}} --icon {{path/to/icon.ico}} {{https://www.google.com/}}`

- 打包一个不可缩放的网页窗口：

`pake --no-resizable {{https://www.google.com/}}`

- 使用全屏模式打包网页：

`pake --fullscreen {{https://www.google.com/}}`

- 使用透明标题栏打包网页：

`pake --transparent {{https://www.google.com/}}`