# adb shell pm list

> 列出软件包管理器中所管理的用户，软件包，权限，插桩测试 (instrumentation)，权限组，功能和库。
> 更多信息：<https://developer.android.com/tools/adb>.

- 列出所有已安装的包：

`adb shell pm list packages`

- 显示系统上的所有用户：

`adb shell pm list users`

- 显示所有已知的权限组：

`adb shell pm list permission-groups`

- 显示所有已知的权限：

`adb shell pm list permissions`

- 显示所有的测试包：

`adb shell pm list instrumentation`

- 显示系统上的所有功能：

`adb shell pm list features`

- 显示当前设备支持的所有库：

`adb shell pm list libraries`
