# lvdisplay

> 显示 Logical Volume Manager (LVM) 逻辑卷的信息。
> 参见：`lvm`。
> 更多信息：<https://manned.org/lvdisplay>。

- 显示所有逻辑卷的信息：

`sudo lvdisplay`

- 显示卷组 vg1 中所有逻辑卷的信息：

`sudo lvdisplay {{vg1}}`

- 显示卷组 vg1 中逻辑卷 lv1 的信息：

`sudo lvdisplay {{vg1/lv1}}`