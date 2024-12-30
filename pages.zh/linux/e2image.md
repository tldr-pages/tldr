# e2image

> 将关键的 ext2/ext3/ext4 文件系统元数据保存到文件中。
> 更多信息：<https://manned.org/e2image>。

- 将设备上的元数据写入特定文件：

`e2image {{/dev/sdXN}} {{path/to/image_file}}`

- 将设备上的元数据打印到 `stdout`：

`e2image {{/dev/sdXN}} -`

- 将文件系统元数据恢复回设备：

`e2image -I {{/dev/sdXN}} {{path/to/image_file}}`

- 创建一个大型的原始稀疏文件，元数据在适当的偏移位置：

`e2image -r {{/dev/sdXN}} {{path/to/image_file}}`

- 创建一个 QCOW2 镜像文件，而不是正常或原始镜像文件：

`e2image -Q {{/dev/sdXN}} {{path/to/image_file}}`