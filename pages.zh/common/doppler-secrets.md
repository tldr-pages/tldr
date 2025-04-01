# doppler secrets

> 管理 Doppler 项目的秘钥。
> 更多信息：<https://docs.doppler.com/docs/accessing-secrets>.

- 获取所有秘钥：

`doppler secrets`

- 获取一个或多个秘钥的值：

`doppler secrets get {{secrets}}`

- 上传秘钥文件：

`doppler secrets upload {{path/to/file.env}}`

- 删除一个或多个秘钥的值：

`doppler secrets delete {{secrets}}`

- 下载秘钥为 `.env` 文件：

`doppler secrets download --format=env --no-file > {{path/to/.env}}`