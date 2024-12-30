# 摇篮部署

> 管理摇篮部署。
> 更多信息：<https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>。

- 将摇篮部署到服务器：

`cradle deploy production`

- 将静态资源部署到 Amazon S3：

`cradle deploy s3`

- 部署包括 Yarn "components" 目录的静态资源：

`cradle deploy s3 --include-yarn`

- 部署包括 "upload" 目录的静态资源：

`cradle deploy s3 --include-upload`