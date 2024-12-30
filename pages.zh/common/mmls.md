# mmls

> 显示卷系统的分区布局。
> 更多信息：<https://wiki.sleuthkit.org/index.php?title=Mmls>。

- 显示存储在映像文件中的分区表：

`mmls {{path/to/image_file}}`

- 显示带有额外分区大小列的分区表：

`mmls -B -i {{path/to/image_file}}`

- 显示拆分的 EWF 映像中的分区表：

`mmls -i ewf {{image.e01}} {{image.e02}}`

- 显示嵌套分区表：

`mmls -t {{nested_table_type}} -o {{offset}} {{path/to/image_file}}`