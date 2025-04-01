# lvcreate

> 在现有的卷组中创建逻辑卷。卷组是逻辑卷和物理卷的集合。
> 相关命令：`lvm`。
> 更多信息：<https://manned.org/lvcreate>。

- 在卷组 vg1 中创建一个 10GB 的逻辑卷：

`lvcreate -L {{10G}} {{vg1}}`

- 在卷组 vg1 中创建一个名为 mylv 的 1500MB 线性逻辑卷：

`lvcreate -L {{1500}} -n {{mylv}} {{vg1}}`

- 在卷组 vg1 中创建一个名为 mylv 的逻辑卷，使用卷组总空间的 60%：

`lvcreate -l {{60%VG}} -n {{mylv}} {{vg1}}`

- 在卷组 vg1 中创建一个名为 mylv 的逻辑卷，使用卷组中所有未分配的空间：

`lvcreate -l {{100%FREE}} -n {{mylv}} {{vg1}}`