# mmls

> 显示卷系统的分区布局。
> 更多信息：<https://wiki.sleuthkit.org/index.php?title=Mmls>.

- 显示存储在镜像文件中的分区表：

`mmls {{path/to/image_file}}`

- 显示带有分区大小附加列的分区表：

`mmls -B -i {{path/to/image_file}}`

- 显示分割的 EWF 镜像中的分区表：

`mmls -i ewf {{image.e01}} {{image.e02}}`

- 显示嵌套的分区表：

`mmls -t {{nested_table_type}} -o {{offset}} {{path/to/image_file}}`