# lynx

> 命令行网页浏览器。
> 更多信息：<https://lynx.browser.org>。

- 访问一个网站：

`lynx {{example.com}}`

- 对匿名账户应用限制：

`lynx -anonymous {{example.com}}`

- 开启鼠标支持（如果可用）：

`lynx -use_mouse {{example.com}}`

- 强制启用颜色模式（如果可用）：

`lynx -color {{example.com}}`

- 打开一个链接，使用特定文件来读写 cookies：

`lynx -cookie_file={{path/to/file}} {{example.com}}`

- 在页面上的链接之间向前和向后导航：

`{{上箭头键|下箭头键}}`

- 返回到上一个显示的页面：

`{{左箭头键|u}}`

- 退出：

`q + y`