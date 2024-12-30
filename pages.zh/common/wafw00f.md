# wafw00f

> 识别和指纹识别保护网站的 Web 应用防火墙 (WAF) 产品。
> 更多信息：<https://github.com/EnableSecurity/wafw00f>。

- 检查一个网站是否使用了任何 WAF：

`wafw00f {{https://www.example.com}}`

- 测试所有可检测的 WAF，而不止于第一个匹配：

`wafw00f --findall {{https://www.example.com}}`

- 通过 [p]roxy（如 BurpSuite）转发请求：

`wafw00f --proxy {{http://localhost:8080}} {{https://www.example.com}}`

- [t] 测试特定的 WAF 产品（运行 `wafw00f -l` 获取所有支持的 WAF 列表）：

`wafw00f --test {{Cloudflare|Cloudfront|Fastly|ZScaler|...}} {{https://www.example.com}}`

- 从文件中传递自定义 [H]eaders：

`wafw00f --headers {{path/to/headers.txt}} {{https://www.example.com}}`

- 从文件中读取目标 [i]nputs 并显示详细输出（多个 `v` 表示更详细的输出）：

`wafw00f --input {{path/to/urls.txt}} -v{{v}}`

- [l] 列出所有可以检测到的 WAF：

`wafw00f --list`