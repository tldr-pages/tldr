# dalfox

> 一个专注于自动化的强大开源XSS扫描器。
> 更多信息：<https://dalfox.hahwul.com/docs/usage>。

- 扫描单个URL以查找XSS漏洞：

`dalfox url {{http://example.com}}`

- 使用头部进行身份验证扫描URL：

`dalfox url {{http://example.com}} -H {{'X-My-Header: 123'}}`

- 从文件中扫描URL列表：

`dalfox file {{path/to/file}}`