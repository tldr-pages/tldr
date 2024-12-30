# drutil

> 与DVD刻录机交互。
> 更多信息：<https://keith.github.io/xcode-man-pages/drutil.1.html>。

- 从驱动器中弹出光盘：

`drutil eject`

- 将目录作为ISO9660文件系统刻录到DVD上。完成时不验证并弹出：

`drutil burn -noverify -eject -iso9660`