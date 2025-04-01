# lwp-request

> 简单的命令行 HTTP 客户端。
> 使用 libwww-perl 构建。
> 更多信息：<https://metacpan.org/pod/lwp-request>。

- 发送简单的 GET 请求：

`lwp-request -m GET {{http://example.com/some/path}}`

- 使用 POST 请求上传文件：

`lwp-request -m POST {{http://example.com/some/path}} < {{path/to/file}}`

- 使用自定义用户代理发送请求：

`lwp-request -H 'User-Agent: {{user_agent}}' -m {{METHOD}} {{http://example.com/some/path}}`

- 使用 HTTP 认证发送请求：

`lwp-request -C {{username}}:{{password}} -m {{METHOD}} {{http://example.com/some/path}}`

- 发送请求并打印请求头：

`lwp-request -U -m {{METHOD}} {{http://example.com/some/path}}`

- 发送请求并打印响应头和状态链：

`lwp-request -E -m {{METHOD}} {{http://example.com/some/path}}`
