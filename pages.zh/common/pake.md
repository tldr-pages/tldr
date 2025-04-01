# pake

> 使用 Rust/Tauri 将任何网页转换为桌面应用程序。
> 更多信息：<https://github.com/tw93/Pake>.

- 封装一个网页：

`pake {{https://www.google.com/}}`

- 以特定窗口大小封装一个网页：

`pake --width {{800}} --height {{600}} {{https://www.google.com/}}`

- 以自定义应用程序名称和图标封装一个网页：

`pake --name {{Google}} --icon {{path/to/icon.ico}} {{https://www.google.com/}}`

- 以不可调整大小的窗口封装一个网页：

`pake --no-resizable {{https://www.google.com/}}`

- 以全屏模式封装一个网页：

`pake --fullscreen {{https://www.google.com/}}`

- 以透明标题栏封装一个网页：

`pake --transparent {{https://www.google.com/}}`
