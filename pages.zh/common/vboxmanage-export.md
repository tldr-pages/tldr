# vboxmanage-export

> 将虚拟机导出为虚拟设备（ISO）或云服务。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>。

- 指定目标 OVA 文件：

`VBoxManage export --output {{path/to/filename.ova}}`

- 以 OVF 0.9 传统模式导出：

`VBoxManage export --legacy09`

- 以 OVF (0.9|1.0|2.0) 格式导出：

`VBoxManage export --{{ovf09|ovf10|ovf20}}`

- 创建导出文件的清单：

`VBoxManage export --manifest`

- 指定 VM 的描述：

`VBoxManage export --description "{{vm_description}}"`