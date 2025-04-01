# cpio

> 将文件复制进出归档文件。
> 支持以下归档格式：cpio 的自定义二进制、旧 ASCII、新 ASCII、crc、HPUX 二进制、HPUX 旧 ASCII、旧 tar 和 POSIX.1 tar。
> 更多信息：<https://www.gnu.org/software/cpio>。

- 从 `stdin` 获取文件名列表并将其添加到 cpio 的二进制格式归档中（复制-[o]ut）：

`echo "{{path/to/file1 path/to/file2 ...}}" | cpio {{[-o|--create]}} > {{archive.cpio}}`

- 复制目录中的所有文件和目录，并将其添加到归档文件中（复制-[o]ut），并以详细模式运行：

`find {{path/to/directory}} | cpio {{[-ov|--create --verbose]}} > {{archive.cpio}}`

- 从归档文件中提取所有文件（复制-[i]n），按需生成目录，并以详细模式运行：

`cpio {{[-idv|--extract --make-directories --verbose]}} < {{archive.cpio}}`