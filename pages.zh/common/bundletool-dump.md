# bundletool dump

> 操作 Android 应用程序包。
> 更多信息：<https://developer.android.com/tools/bundletool>。

- 显示基础模块的 `AndroidManifest.xml`：

`bundletool dump manifest --bundle {{path/to/bundle.aab}}`

- 使用 XPath 显示 `AndroidManifest.xml` 中的特定值：

`bundletool dump manifest --bundle {{path/to/bundle.aab}} --xpath {{/manifest/@android:versionCode}}`

- 显示特定模块的 `AndroidManifest.xml`：

`bundletool dump manifest --bundle {{path/to/bundle.aab}} --module {{name}}`

- 显示应用程序包中的所有资源：

`bundletool dump resources --bundle {{path/to/bundle.aab}}`

- 显示特定资源的配置：

`bundletool dump resources --bundle {{path/to/bundle.aab}} --resource {{type/name}}`

- 使用 ID 显示特定资源的配置和数值：

`bundletool dump resources --bundle {{path/to/bundle.aab}} --resource {{0x7f0e013a}} --values`

- 显示包配置文件的内容：

`bundletool dump config --bundle {{path/to/bundle.aab}}`