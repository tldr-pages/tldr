# czkawka-cli

> `czkawka` 的命令行版本，是一个多功能应用程序，用于查找重复文件、空文件夹、相似图像等更多功能。
> 更多信息：<https://github.com/qarmin/czkawka>。

- 列出特定目录中的重复或相似文件：

`czkawka-cli {{dup|image}} --directories {{path/to/directory1 path/to/directory2 ...}}`

- 在特定目录中查找重复文件并删除它们（默认：`NONE`）：

`czkawka-cli dup --directories {{path/to/directory1 path/to/directory2 ...}} --delete-method {{AEN|AEO|ON|OO|HARD|NONE}}`