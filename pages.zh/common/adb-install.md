# adb install

> 安卓调试桥 -Install: 将应用安装包推送到 Android 模拟器或已连接的安卓设备。
> 更多信息：<https://developer.android.com/studio/command-line/adb>.

- 向模拟器/设备推送安卓 app：

`adb install {{路径/到/应用.apk}}`

- 重装 app, 保持原有数据：

`adb install -r {{路径/到/应用.apk}}`

- 授予 app manifest 中列举的所有权限许可：

`adb install -g {{路径/到/应用.apk}}`

- 快速部署模式，仅更新 APK 更改过的部分：

`adb install --fastdeploy {{路径/到/应用.apk}}`
