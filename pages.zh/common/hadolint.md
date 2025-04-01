# hadolint

> Dockerfile 代码检查工具。
> 更多信息：<https://github.com/hadolint/hadolint>。

- 检查 Dockerfile：

`hadolint {{path/to/Dockerfile}}`

- 检查 Dockerfile，并以 JSON 格式输出结果：

`hadolint --format {{json}} {{path/to/Dockerfile}}`

- 检查 Dockerfile，并以指定的格式输出结果：

`hadolint --format {{tty|json|checkstyle|codeclimate|codacy}} {{path/to/Dockerfile}}`

- 检查 Dockerfile，忽略特定的规则：

`hadolint --ignore {{DL3006}} --ignore {{DL3008}} {{path/to/Dockerfile}}`

- 使用特定的可信注册表检查多个 Dockerfile：

`hadolint --trusted-registry {{docker.io}} --trusted-registry {{example.com}}:{{5000}} {{path/to/Dockerfile1 path/to/Dockerfile2 ...}}`