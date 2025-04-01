# apkeep

> 从各种来源下载 APK 文件。
> 更多信息：<https://github.com/EFForg/apkeep>.

- 将 APK 文件下载到指定目录：

`apkeep --app {{com.example.application}} {{path/to/directory}}`

- 列出所有可用的版本以供下载：

`apkeep --app {{com.example.application}} --list-versions {{path/to/directory}}`

- 指定下载来源的商店：

`apkeep --app {{com.example.application}} --download-source {{apk-pure|google-play|f-droid|huawei-app-gallery}} {{path/to/directory}}`
