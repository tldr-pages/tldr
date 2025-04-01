# whatweb

> 下一代 Web 扫描器。
> 更多信息：<https://morningstarsecurity.com/research/whatweb>。

- 扫描网站/目标以检测 Web 技术：

`whatweb {{website1 website2 ...}}`

- 从文件中读取目标/网站：

`whatweb -i {{targets_file}}`

- 以详细模式扫描网站/目标：

`whatweb -v {{example.com}}`

- 对网站进行积极扫描：

`whatweb -a 3 {{example.com}}`

- 扫描网络并抑制错误：

`whatweb --no-errors {{192.168.0.0/24}}`

- 列出插件：

`whatweb -l`

- 列出插件详细信息：

`whatweb -I {{plugin_name}}`