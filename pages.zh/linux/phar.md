# phar

> 创建、更新或解压 PHP 归档文件（PHAR）。
> 更多信息：<https://manned.org/phar>.

- 向 Phar 文件中添加一个或多个文件或目录：

`phar add -f {{path/to/phar_file}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 显示 Phar 文件的内容：

`phar list -f {{path/to/phar_file}}`

- 从 Phar 文件中删除指定的文件或目录：

`phar delete -f {{path/to/phar_file}} -e {{file_or_directory}}`

- 压缩或解压缩 Phar 文件中的文件和目录：

`phar compress -f {{path/to/phar_file}} -c {{algorithm}}`

- 获取 Phar 文件的信息：

`phar info -f {{path/to/phar_file}}`

- 使用特定的哈希算法签名 Phar 文件：

`phar sign -f {{path/to/phar_file}} -h {{algorithm}}`

- 使用 OpenSSL 私钥签名 Phar 文件：

`phar sign -f {{path/to/phar_file}} -h openssl -y {{path/to/private_key}}`

- 显示帮助信息和可用的哈希/压缩算法：

`phar help`
