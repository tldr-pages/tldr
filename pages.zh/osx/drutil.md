# drutil

> 与DVD刻录机交互.

- 从驱动器中弹出磁盘:

`drutil eject`

- 将目录作为iso9660文件系统刻录到DVD上. 完成后不验证和弹出:

`drutil burn -noverify -eject -iso9660`
