# 微软边缘浏览器

> 由微软开发的现代网页浏览器，基于谷歌开发的Chromium网页浏览器。
> 在Windows中，此命令可作为`msedge`使用。
> 注意：来自`chromium`的附加命令参数也可以用于控制微软边缘浏览器。
> 更多信息：<https://microsoft.com/edge>。

- 打开特定的URL或文件：

`microsoft-edge {{https://example.com|path/to/file.html}}`

- 在InPrivate模式下打开：

`microsoft-edge --inprivate {{example.com}}`

- 在新窗口中打开：

`microsoft-edge --new-window {{example.com}}`

- 以应用程序模式打开（无工具栏、URL栏、按钮等）：

`microsoft-edge --app={{https://example.com}}`

- 使用代理服务器：

`microsoft-edge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 使用自定义配置文件目录打开：

`microsoft-edge --user-data-dir={{path/to/directory}}`

- 无需CORS验证打开（有助于测试API）：

`microsoft-edge --user-data-dir={{path/to/directory}} --disable-web-security`

- 为每个打开的标签页自动打开开发者工具窗口：

`microsoft-edge --auto-open-devtools-for-tabs`