# immich-go

> Immich-Go 是一个开源工具，旨在简化将大量照片集合上传到自托管的 Immich 服务器。
> 参见: `immich-cli`。
> 更多信息: <https://github.com/simulot/immich-go>。

- 上传 Google Photos 备份文件到 Immich 服务器:

`immich-go -server={{server_url}} -key={{server_key}} upload {{path/to/takeout_file.zip}}`

- 导入 2019 年 6 月拍摄的照片，并自动生成相册:

`immich-go -server={{server_url}} -key={{server_key}} upload -create-albums -google-photos -date={{2019-06}} {{path/to/takeout_file.zip}}`

- 使用配置文件中的服务器和密钥上传备份文件:

`immich-go -use-configuration={{~/.immich-go/immich-go.json}} upload {{path/to/takeout_file.zip}}`

- 检查 Immich 服务器内容，删除质量较低的图片，并保留相册:

`immich-go -server={{server_url}} -key={{server_key}} duplicate -yes`

- 删除名称格式为 "YYYY-MM-DD" 的所有相册:

`immich-go -server={{server_url}} -key={{server_key}} tool album delete {{\d{4}-\d{2}-\d{2}}}`