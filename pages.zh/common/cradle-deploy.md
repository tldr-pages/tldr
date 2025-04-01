# cradle deploy

> 管理 Cradle 部署。
> 更多信息：<https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>。

- 将 Cradle 部署到服务器：

`cradle deploy production`

- 将静态资源部署到 Amazon S3：

`cradle deploy s3`

- 将静态资源（包括 Yarn 的 "components" 目录）部署到 Amazon S3：

`cradle deploy s3 --include-yarn`

- 将静态资源（包括 "upload" 目录）部署到 Amazon S3：

`cradle deploy s3 --include-upload`