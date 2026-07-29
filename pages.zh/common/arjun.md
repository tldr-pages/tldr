# arjun

> 发现 Web 应用程序的 HTTP 参数。
> 更多信息：<https://github.com/s0md3v/Arjun/wiki/Usage>。

- 扫描 URL 的 GET 参数：

`arjun -u {{https://example.com/page.php}}`

- 使用 POST 方法扫描：

`arjun -u {{https://example.com/api}} -m POST`

- 将发现的参数保存到 JSON 文件：

`arjun -u {{https://example.com}} -o {{路径/到/output.json}}`

- 使用自定义字典：

`arjun -u {{https://example.com}} -w {{路径/到/wordlist.txt}}`

- 增加请求延迟以避免速率限制：

`arjun -u {{https://example.com}} -d {{2}}`
