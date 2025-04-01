# engrampa

> 在 MATE 桌面环境中将文件打包为 zip/tar 文件。
> 参见：`zip`，`tar`。
> 更多信息：<https://github.com/mate-desktop/engrampa>。

- 启动 Engrampa：

`engrampa`

- 打开指定的压缩文件：

`engrampa {{/路径/到/压缩文件1.tar /路径/到/压缩文件2.tar ...}}`

- 递归地将指定的文件和/或目录添加到压缩文件中：

`engrampa --add-to={{/路径/到/压缩文件.tar}} {{/路径/到/文件或目录1 /路径/到/文件或目录2 ...}}`

- 从压缩文件中将文件和/或目录解压到指定路径：

`engrampa --extract-to={{/路径/到/目录}} {{/路径/到/压缩文件1.tar /路径/到/压缩文件2.tar ...}}`