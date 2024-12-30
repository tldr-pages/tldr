# docker secret

> 管理 Docker swarm 秘密。
> 更多信息：<https://docs.docker.com/reference/cli/docker/secret/>.

- 从 `stdin` 创建一个新秘密：

`{{command}} | docker secret create {{secret_name}} -`

- 从文件创建一个新秘密：

`docker secret create {{secret_name}} {{path/to/file}}`

- 列出所有秘密：

`docker secret ls`

- 以人类友好的格式显示一个或多个秘密的详细信息：

`docker secret inspect --pretty {{secret_name1 secret_name2 ...}}`

- 移除一个或多个秘密：

`docker secret rm {{secret_name1 secret_name2 ...}}`