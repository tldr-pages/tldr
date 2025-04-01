# virt-xml

> 使用显式的命令行选项编辑 libvirt 域 XML 文件。
> 注意：'domain' 指的是现有虚拟机的名称、UUID 或 ID（参见：tldr virsh）。
> 更多信息：<https://github.com/virt-manager/virt-manager/blob/main/man/virt-xml.rst>。

- 列出特定选项的所有子选项：

`virt-xml --{{option}}=?`

- 列出磁盘、网络和启动的所有子选项：

`virt-xml --disk=? --network=? --boot=?`

- 编辑特定域的值：

`virt-xml {{domain}} --edit --{{option}} {{suboption}}={{new_value}}`

- 更改特定域的描述：

`virt-xml {{domain}} --edit --metadata description="{{new_description}}"`

- 为特定域启用/禁用引导设备菜单：

`virt-xml {{domain}} --edit --boot bootmenu={{on|off}}`

- 将主机 USB 集线器连接到运行中的虚拟机（参见：tldr lsusb）：

`virt-xml {{domain}} --update --add-device --hostdev {{bus}}.{{device}}`