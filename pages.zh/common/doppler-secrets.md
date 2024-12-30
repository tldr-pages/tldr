# Doppler 秘密

> 管理您的 Doppler 项目的秘密。
> 更多信息：<https://docs.doppler.com/docs/accessing-secrets>。

- 获取所有秘密：

`doppler secrets`

- 获取一个或多个秘密的值：

`doppler secrets get {{secrets}}`

- 上传秘密文件：

`doppler secrets upload {{path/to/file.env}}`

- 删除一个或多个秘密的值：

`doppler secrets delete {{secrets}}`

- 将秘密下载为 `.env` 格式：

`doppler secrets download --format=env --no-file > {{path/to/.env}}`