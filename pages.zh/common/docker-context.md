# docker context

> 在多个 Docker 环境之间切换。
> 更多信息：<https://docs.docker.com/reference/cli/docker/context/>.

- 使用特定的 Docker 端点创建一个上下文：

`docker context create {{my_context}} --docker "host={{tcp://remote-host:2375}}"`

- 基于 `DOCKER_HOST` 环境变量创建一个上下文：

`docker context create {{my_context}}`

- 切换到一个上下文：

`docker context use {{my_context}}`

- 列出所有上下文：

`docker context ls`