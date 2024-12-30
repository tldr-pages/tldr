# asr

> 将磁盘映像还原（复制）到卷上。
> 此命令名称代表 Apple 软件还原。
> 更多信息：<https://keith.github.io/xcode-man-pages/asr.8.html>。

- 将磁盘映像还原到目标卷：

`sudo asr restore --source {{image_file.dmg}} --target {{path/to/volume_file}}`

- 在还原之前擦除目标卷：

`sudo asr restore --source {{image_file.dmg}} --target {{path/to/volume_file}} --erase`

- 在还原后跳过验证：

`sudo asr restore --source {{image_file.dmg}} --target {{path/to/volume_file}} --noverify`

- 在不使用中间磁盘映像的情况下克隆卷：

`sudo asr restore --source {{path/to/volume_file}} --target {{path/to/volume_file}}`