# vboxmanage-controlvm

> 更改正在运行的虚拟机的状态和设置。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-controlvm>。

- 暂停虚拟机的执行：

`VBoxManage controlvm {{uuid|vm_name}} pause`

- 恢复已暂停的虚拟机的执行：

`VBoxManage controlvm {{uuid|vm_name}} resume`

- 对虚拟机执行冷重启：

`VBoxManage controlvm {{uuid|vm_name}} reset`

- 以拔掉电源线的效果关闭虚拟机：

`VBoxManage controlvm {{uuid|vm_name}} poweroff`

- 关闭虚拟机并保存当前状态：

`VBoxManage controlvm {{uuid|vm_name}} savestate`

- 向虚拟机发送 ACPI（高级配置和电源接口）关机信号：

`VBoxManage controlvm {{uuid|vm_name}} acpipowerbutton`

- 向客户操作系统发送重启命令：

`VBoxManage controlvm {{uuid|vm_name}} reboot`

- 关闭虚拟机但不保存状态：

`VBoxManage controlvm {{uuid|vm_name}} shutdown`
