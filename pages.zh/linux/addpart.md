# addpart

> 告诉Linux内核指定分区的存在。
> 这是一个简单的`add partition` ioctl的封装。
> 更多信息：<https://manned.org/addpart>。

- 告诉内核指定分区的存在：

`addpart {{设备}} {{分区}} {{起始}} {{长度}}`