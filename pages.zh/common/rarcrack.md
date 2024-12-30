# rarcrack

> 用于 RAR、Zip 和 7z 压缩文件的密码破解工具。

- 对压缩文件进行暴力破解密码（尝试猜测压缩文件类型）：

`rarcrack {{path/to/file.zip}}`

- 指定压缩文件类型：

`rarcrack --type {{rar|zip|7z}} {{path/to/file.zip}}`

- 使用多个线程：

`rarcrack --threads {{6}} {{path/to/file.zip}}`