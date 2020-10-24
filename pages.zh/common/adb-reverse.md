# adb reverse

> Android Debug Bridge Reverse: reverse socket connections from an Android emulator instance or connected Android devices.
> 详见: <https://developer.android.com/studio/command-line/adb>.

- 显示所有来自设备的(DEVICE —> PC)映射的端口连接列表

`adb reverse —list`

- 反向映射端口连接(DEVICE —> PC)

`adb reverse (remote) (local)`

`adb reverse tcp:7000 tcp:5000`

- 如果local已经映射了就会失败

`adb reverse —no-rebind (remote) (local)`

`adb reverse --no-rebind tcp:7000 tcp:5000`

- 移除指定的反向映射端口连接

`adb reverse —remove tcp:7000`

`adb reverse —remove-all`
