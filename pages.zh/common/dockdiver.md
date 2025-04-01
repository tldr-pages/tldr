# dockdiver

> 一个用于与 Docker 注册表交互的工具，包括列出和转储仓库。
> 更多信息：<https://github.com/MachiavelliII/dockdiver>.

- 列出 Docker 注册表中的所有仓库：

`dockdiver -url {{http://target}} -list`

- 将特定仓库转储到默认输出目录（docker_dump）：

`dockdiver -url {{http://target}} -dump {{repository_name}}`

- 使用基本认证转储所有仓库：

`dockdiver -url {{http://example.com}} -dump-all -username {{username}} -password {{password}}`

- 使用自定义端口和速率限制转储仓库：

`dockdiver -url http://example.com -dump {{repository_name}} -port {{port}} -rate {{requests_per_second}} -dir {{path/to/output_directory}}`

- 使用 Bearer 令牌进行授权并转储所有仓库：

`dockdiver -url {{http://example.com}} -dump-all -bearer {{bearer_token}}`

- 以 JSON 格式添加自定义头部（例如，`'{"X-Custom": "Value"}'`）：

`dockdiver -url {{http://example.com}} -list -headers {{'{"X-Custom": "Value"}'}}`