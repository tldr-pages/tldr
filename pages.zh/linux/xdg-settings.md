# xdg-settings

> 管理 XDG 兼容桌面环境的设置。
> 更多信息：<https://portland.freedesktop.org/doc/xdg-settings.html>.

- 打印默认的网页浏览器：

`xdg-settings get {{default-web-browser}}`

- 设置默认的网页浏览器为 Firefox：

`xdg-settings set {{default-web-browser}} {{firefox.desktop}}`

- 设置默认的邮件 URL 方案处理器为 Evolution：

`xdg-settings set {{default-url-scheme-handler}} {{mailto}} {{evolution.desktop}}`

- 设置默认的 PDF 文档查看器：

`xdg-settings set {{pdf-viewer.desktop}}`

- 显示帮助：

`xdg-settings --help`