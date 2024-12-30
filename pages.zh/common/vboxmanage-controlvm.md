# vboxmanage-controlvm

> 更改当前运行虚拟机的状态和设置。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-controlvm>。

- 暂停虚拟机的执行：

`VBoxManage controlvm {{uuid|vm_name}} pause`

- 恢复已暂停虚拟机的执行：

`VBoxManage controlvm {{uuid|vm_name}} resume`

- 对虚拟机执行冷重置：

`VBoxManage controlvm {{uuid|vm_name}} reset`

- 关闭虚拟机，效果与拔掉计算机电源线相同：

`VBoxManage controlvm {{uuid|vm_name}} poweroff`

- 关闭虚拟机并保存其当前状态：

`VBoxManage controlvm {{uuid|vm_name}} savestate`

- 向虚拟机发送 ACPI（高级配置和电源接口）关机信号：

`VBoxManage controlvm {{uuid|vm_name}} acpipowerbutton`

- 向客人操作系统发送重启命令：

`VBoxManage controlvm {{uuid|vm_name}} reboot`

- 关闭虚拟机而不保存其状态：

`VBoxManage controlvm {{uuid|vm_name}} shutdown`