# adb shell pm

> 安卓软件包管理工具。
> 更多信息：<https://developer.android.com/tools/adb>.

- 列出已安装的包：

`adb shell pm list packages`

- 从指定路径，安装软件包：

`adb shell pm install /{{路径/到/软件包.apk}}`

- 从设备卸载一个包：

`adb shell pm uninstall {{软件包}}`

- 清除单个软件包的所有数据文件：

`adb shell pm clear {{软件包}}`

- 启用软件包或组件：

`adb shell pm enable {{包名_或_类名}}`

- 禁用软件包或组件：

`adb shell pm disable-user {{包名_或_类名}}`

- 为应用授予权限：

`adb shell pm grant {{包名}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- 撤销应用权限：

`adb shell pm revoke {{包名}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
