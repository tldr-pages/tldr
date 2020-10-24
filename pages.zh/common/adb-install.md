# adb install

> Android Debug Bridge Install: 推送安装包到Android模拟器或已连接的安卓设备.
> 详见: <https://developer.android.com/studio/command-line/adb>.

- 向模拟器/设备推送安卓app:

`adb install {{path/to/file.apk}}`

- 重装app, 保持原有数据:

`adb install -r {{path/to/file.apk}}`

- 授予app manifest中列举的所有权限许可:

`adb install -g {{path/to/file.apk}}`

- 快速部署模式，仅更新APK更改过的部分:

`adb install --fastdeploy {{path/to/file.apk}}`
