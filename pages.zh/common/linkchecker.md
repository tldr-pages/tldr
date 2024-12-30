# 链接检查器

> 检查 HTML 文档和网站中断链的命令行客户端。
> 更多信息：<https://linkchecker.github.io/linkchecker/>。

- 查找 <https://example.com/> 上的断链：

`linkchecker {{https://example.com/}}`

- 还检查指向外部域的 URL：

`linkchecker --check-extern {{https://example.com/}}`

- 忽略与特定正则表达式匹配的 URL：

`linkchecker --ignore-url {{regular_expression}} {{https://example.com/}}`

- 将结果输出到 CSV 文件：

`linkchecker --file-output {{csv}}/{{path/to/file}} {{https://example.com/}}`