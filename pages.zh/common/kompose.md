# kompose

> 将docker-compose应用程序转换为Kubernetes。
> 更多信息：<https://github.com/kubernetes/kompose>。

- 将容器化应用程序部署到Kubernetes：

`kompose up -f {{docker-compose.yml}}`

- 从Kubernetes中删除已实例化的服务/部署：

`kompose down -f {{docker-compose.yml}}`

- 将docker-compose文件转换为Kubernetes资源文件：

`kompose convert -f {{docker-compose.yml}}`