# apkeep

> 从多个来源下载APK文件。
> 更多信息：<https://github.com/EFForg/apkeep>。

- 将APK文件下载到指定目录：

`apkeep --app {{com.example.application}} {{path/to/directory}}`

- 列出所有可供下载的版本：

`apkeep --app {{com.example.application}} --list-versions {{path/to/directory}}`

- 指定下载来源的商店：

`apkeep --app {{com.example.application}} --download-source {{apk-pure|google-play|f-droid|huawei-app-gallery}} {{path/to/directory}}`