# electron-packager

> 为 Windows、Linux 和 macOS 构建 Electron 应用程序可执行文件。
> 需要在应用程序目录中包含有效的 package.json 文件。
> 更多信息：<https://github.com/electron/electron-packager>。

- 为当前架构和平台打包应用程序：

`electron-packager "{{path/to/app}}" "{{app_name}}"`

- 为所有架构和平台打包应用程序：

`electron-packager "{{path/to/app}}" "{{app_name}}" --all`

- 为 64 位 Linux 打包应用程序：

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{linux}}" --arch="{{x64}}"`

- 为 ARM 架构的 macOS 打包应用程序：

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{darwin}}" --arch="{{arm64}}"`