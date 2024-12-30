# virt-xml

> 使用明确的命令行选项编辑libvirt域XML文件。
> 注意：'域'指的是现有虚拟机的名称、UUID或ID（参见：tldr virsh）。
> 更多信息：<https://github.com/virt-manager/virt-manager/blob/main/man/virt-xml.rst>。

- 列出特定选项的所有子选项：

`virt-xml --{{option}}=?`

- 列出磁盘、网络和引导的所有子选项：

`virt-xml --disk=? --network=? --boot=?`

- 编辑特定域的值：

`virt-xml {{domain}} --edit --{{option}} {{suboption}}={{new_value}}`

- 更改特定域的描述：

`virt-xml {{domain}} --edit --metadata description="{{new_description}}"`

- 启用/禁用特定域的引导设备菜单：

`virt-xml {{domain}} --edit --boot bootmenu={{on|off}}`

- 将主机USB集线器连接到正在运行的虚拟机（参见：tldr lsusb）：

`virt-xml {{domain}} --update --add-device --hostdev {{bus}}.{{device}}`