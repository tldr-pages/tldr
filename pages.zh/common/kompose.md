# kompose

> 将 docker-compose 应用程序转换为 Kubernetes。
> 更多信息：<https://github.com/kubernetes/kompose>。

- 将容器化的应用程序部署到 Kubernetes：

`kompose up -f {{docker-compose.yml}}`

- 从 Kubernetes 删除已实例化的服务/部署：

`kompose down -f {{docker-compose.yml}}`

- 将 docker-compose 文件转换为 Kubernetes 资源文件：

`kompose convert -f {{docker-compose.yml}}`