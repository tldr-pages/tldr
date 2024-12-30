# hadolint

> Dockerfile 代码检查工具。
> 更多信息请访问: <https://github.com/hadolint/hadolint>。

- 检查一个 Dockerfile：

`hadolint {{path/to/Dockerfile}}`

- 检查一个 Dockerfile，并以 JSON 格式显示输出：

`hadolint --format {{json}} {{path/to/Dockerfile}}`

- 检查一个 Dockerfile，并以特定格式显示输出：

`hadolint --format {{tty|json|checkstyle|codeclimate|codacy}} {{path/to/Dockerfile}}`

- 检查一个 Dockerfile，忽略特定规则：

`hadolint --ignore {{DL3006}} --ignore {{DL3008}} {{path/to/Dockerfile}}`

- 使用特定的受信任注册表检查多个 Dockerfile：

`hadolint --trusted-registry {{docker.io}} --trusted-registry {{example.com}}:{{5000}} {{path/to/Dockerfile1 path/to/Dockerfile2 ...}}`