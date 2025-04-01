# lynx

> 命令行网页浏览器。
> 更多信息：<https://lynx.browser.org>。

- 访问一个网站：

`lynx {{example.com}}`

- 为匿名账户应用限制：

`lynx -anonymous {{example.com}}`

- 如果可用，启用鼠标支持：

`lynx -use_mouse {{example.com}}`

- 如果可用，强制启用颜色模式：

`lynx -color {{example.com}}`

- 使用特定文件读取和写入cookies来打开链接：

`lynx -cookie_file={{path/to/file}} {{example.com}}`

- 通过页面上的链接前后导航：

`{{<ArrowUp>|<ArrowDown>}}`

- 返回上一个显示的页面：

`{{<ArrowLeft>|<u>}}`

- 退出：

`<q><y>`
