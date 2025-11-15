# drutil

> 与 DVD 刻录机交互。
> 更多信息：<https://keith.github.io/xcode-man-pages/drutil.1.html>.

- 从驱动器中弹出磁盘：

`drutil eject`

- 将目录作为 iso9660 文件系统刻录到 DVD 上。完成后不验证和弹出：

`drutil burn -noverify -eject -iso9660`
