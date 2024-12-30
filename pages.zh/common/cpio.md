# cpio

> 在归档中复制文件。
> 支持以下归档格式：cpio 的自定义二进制格式、旧 ASCII、新 ASCII、crc、HPUX 二进制、HPUX 旧 ASCII、旧 tar 和 POSIX.1 tar。
> 更多信息：<https://www.gnu.org/software/cpio>。

- 从 `stdin` 获取文件名列表，并将它们添加到 cpio 的二进制格式归档中：

`echo "{{path/to/file1 path/to/file2 ...}}" | cpio -o > {{archive.cpio}}`

- 复制目录中的所有文件和目录，并以 [v]erbose 模式将它们添加到归档中：

`find {{path/to/directory}} | cpio -ov > {{archive.cpio}}`

- 从归档中 P[i]ck 所有文件，在需要的地方生成 [d]irectories，以 [v]erbose 模式：

`cpio -idv < {{archive.cpio}}`