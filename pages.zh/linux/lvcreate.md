# lvcreate

> 在现有的卷组中创建一个逻辑卷。卷组是逻辑卷和物理卷的集合。
> 另见：`lvm`。
> 更多信息：<https://manned.org/lvcreate>。

- 在卷组 vg1 中创建一个 10 吉字节的逻辑卷：

`lvcreate -L {{10G}} {{vg1}}`

- 在卷组 vg1 中创建一个名为 mylv 的 1500 兆字节线性逻辑卷：

`lvcreate -L {{1500}} -n {{mylv}} {{vg1}}`

- 创建一个名为 mylv 的逻辑卷，使用卷组 vg1 中总空间的 60%：

`lvcreate -l {{60%VG}} -n {{mylv}} {{vg1}}`

- 创建一个名为 mylv 的逻辑卷，使用卷组 vg1 中所有未分配的空间：

`lvcreate -l {{100%FREE}} -n {{mylv}} {{vg1}}`