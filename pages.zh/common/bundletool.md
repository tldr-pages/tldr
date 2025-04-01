# bundletool

> 管理 Android 应用程序包。
> 某些子命令（如 `validate`）有自己的使用文档。
> 更多信息：<https://developer.android.com/tools/bundletool>.

- 显示子命令的帮助信息：

`bundletool help {{subcommand}}`

- 从应用程序包生成 APK（提示输入密钥库密码）：

`bundletool build-apks --bundle {{path/to/bundle.aab}} --ks {{path/to/key.keystore}} --ks-key-alias {{key_alias}} --output {{path/to/file.apks}}`

- 从应用程序包生成 APK 并提供密钥库密码：

`bundletool build-apks --bundle {{path/to/bundle.aab}} --ks {{path/to/key.keystore}} --ks-key-alias {{key_alias}} --ks-pass {{pass:the_password}} --output {{path/to/file.apks}}`

- 生成仅包含一个通用 APK 的 APK 文件：

`bundletool build-apks --bundle {{path/to/bundle.aab}} --mode {{universal}} --ks {{path/to/key.keystore}} --ks-key-alias {{key_alias}} --output {{path/to/file.apks}}`

- 在模拟器或设备上安装合适的 APK 组合：

`bundletool install-apks --apks {{path/to/file.apks}}`

- 估算应用程序的下载大小：

`bundletool get-size total --apks {{path/to/file.apks}}`

- 为模拟器或设备生成设备规格的 JSON 文件：

`bundletool get-device-spec --output {{path/to/file.json}}`

- 验证应用程序包并显示详细信息：

`bundletool validate --bundle {{path/to/bundle.aab}}`