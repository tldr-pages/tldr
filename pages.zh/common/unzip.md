# 解压缩

> 从Zip档案中提取文件/目录。
> 另见：`zip`。
> 更多信息：<https://manned.org/unzip>。

- 将特定档案中的所有文件/目录提取到当前目录：

`unzip {{path/to/archive1.zip path/to/archive2.zip ...}}`

- 将档案中的文件/目录提取到特定路径：

`unzip {{path/to/archive1.zip path/to/archive2.zip ...}} -d {{path/to/output}}`

- 将档案中的文件/目录提取到`stdout`及提取的文件名：

`unzip -c {{path/to/archive1.zip path/to/archive2.zip ...}}`

- 提取在Windows上创建的档案，其中包含非ASCII（例如中文或日文字符）文件名的文件：

`unzip -O {{gbk}} {{path/to/archive1.zip path/to/archive2.zip ...}}`

- 列出特定档案的内容而不提取它们：

`unzip -l {{path/to/archive.zip}}`

- 从档案中提取特定文件：

`unzip -j {{path/to/archive.zip}} {{path/to/file1_in_archive path/to/file2_in_archive ...}}`