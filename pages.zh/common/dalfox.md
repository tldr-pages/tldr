# dalfox

> 一个强大的开源 XSS 扫描器，专注于自动化。
> 更多信息：<https://dalfox.hahwul.com/docs/usage>。

- 扫描单个 URL 的 XSS 漏洞：

`dalfox url {{http://example.com}}`

- 使用头部信息进行身份验证来扫描 URL：

`dalfox url {{http://example.com}} -H {{'X-My-Header: 123'}}`

- 从文件中扫描多个 URL：

`dalfox file {{path/to/file}}`