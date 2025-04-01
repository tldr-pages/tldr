# rarcrack

> 解压 RAR、Zip 和 7z 文件的密码破解工具。

- 穷举破解存档文件的密码（尝试猜测存档类型）：

`rarcrack {{path/to/file.zip}}`

- 指定存档文件类型：

`rarcrack --type {{rar|zip|7z}} {{path/to/file.zip}}`

- 使用多个线程进行破解：

`rarcrack --threads {{6}} {{path/to/file.zip}}`
