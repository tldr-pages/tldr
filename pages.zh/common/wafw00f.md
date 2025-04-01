# wafw00f

> 识别和指纹识别保护网站的 Web 应用防火墙（WAF）产品。
> 更多信息：<https://github.com/EnableSecurity/wafw00f/wiki/Usage#arguments-list>.

- 检查网站是否使用了任何 WAF：

`wafw00f {{https://www.example.com}}`

- 测试所有可检测的 WAF，不因首次匹配而停止：

`wafw00f {{[-a|--findall]}} {{https://www.example.com}}`

- 通过代理（如 BurpSuite）传递请求：

`wafw00f {{[-p|--proxy]}} {{http://localhost:8080}} {{https://www.example.com}}`

- 测试特定的 WAF 产品（运行 `wafw00f -l` 获取所有支持的 WAF 列表）：

`wafw00f {{[-t|--test]}} {{Cloudflare|Cloudfront|Fastly|ZScaler|...}} {{https://www.example.com}}`

- 从文件中传递自定义头部：

`wafw00f {{[-H|--headers]}} {{path/to/headers.txt}} {{https://www.example.com}}`

- 从文件中读取目标输入并显示详细输出（多个 `v` 表示更多的详细信息）：

`wafw00f {{[-i|--input]}} {{path/to/urls.txt}} -{{vv}}`

- 列出所有可检测的 WAF：

`wafw00f {{[-l|--list]}}`
