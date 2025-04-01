# waydroid

> 一种基于容器的方法，在常规的 Linux 系统（如 Ubuntu）上启动完整的 Android 系统。
> 更多信息：<https://docs.waydro.id>。

- 启动 Waydroid:

`waydroid`

- 初始化 Waydroid（首次运行或重新安装 Android 时必需）:

`sudo waydroid init`

- 从文件安装新的 Android 应用:

`waydroid app install {{path/to/file.apk}}`

- 通过包名启动 Android 应用:

`waydroid app launch {{com.example.app}}`

- 启动或停止 Waydroid 会话:

`waydroid session {{start|stop}}`

- 管理 Waydroid 容器:

`sudo waydroid container {{start|stop|restart|freeze|unfreeze}}`

- 打开 Waydroid Shell:

`sudo waydroid shell`

- 调整 Waydroid 窗口尺寸:

`waydroid prop set persist.waydroid.{{width|height}} {{number}}`