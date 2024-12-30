# zipnote

> 查看、添加或编辑 Zip 压缩包的注释。
> 文件在 Zip 压缩包中也可以被重命名。
> 更多信息：<https://manned.org/zipnote>.

- 查看 Zip 压缩包中的注释：

`zipnote {{路径/到/文件.zip}}`

- 将 Zip 压缩包中的注释提取到一个文件：

`zipnote {{路径/到/文件.zip}} > {{路径/到/文件.txt}}`

- 从一个文件中添加/更新 Zip 压缩包中的注释：

`zipnote -w {{路径/到/文件.zip}} < {{路径/到/文件.txt}}`
