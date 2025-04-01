# e2image

> 保存 ext2/ext3/ext4 文件系统的元数据到文件。
> 更多信息：<https://manned.org/e2image>.

- 将设备上的元数据写入特定文件：

`e2image {{/dev/sdXN}} {{path/to/image_file}}`

- 将设备上的元数据打印到 `stdout`：

`e2image {{/dev/sdXN}} -`

- 将文件系统元数据恢复到设备：

`e2image -I {{/dev/sdXN}} {{path/to/image_file}}`

- 创建一个具有正确偏移量的大型稀疏原始文件：

`e2image -r {{/dev/sdXN}} {{path/to/image_file}}`

- 创建一个 QCOW2 镜像文件而不是普通或原始镜像文件：

`e2image -Q {{/dev/sdXN}} {{path/to/image_file}}`
