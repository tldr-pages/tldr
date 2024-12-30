# aws s3 网站

> 为一个桶设置网站配置。
> 另见：`aws s3`。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/s3/website.html>。

- 将桶配置为静态网站：

`aws s3 website {{s3://桶名称}} --index-document {{index.html}}`

- 为网站配置错误页面：

`aws s3 website {{s3://桶名称}} --index-document {{index.html}} --error-document {{error.html}}`