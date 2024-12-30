# phar

> 创建、更新或提取 PHP 压缩包 (PHAR)。
> 更多信息: <https://manned.org/phar>。

- 将一个或多个文件或目录添加到 Phar 文件中：

`phar add -f {{path/to/phar_file}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 显示 Phar 文件的内容：

`phar list -f {{path/to/phar_file}}`

- 从 Phar 文件中删除指定的文件或目录：

`phar delete -f {{path/to/phar_file}} -e {{file_or_directory}}`

- 压缩或解压缩 Phar 文件中的文件和目录：

`phar compress -f {{path/to/phar_file}} -c {{algorithm}}`

- 获取有关 Phar 文件的信息：

`phar info -f {{path/to/phar_file}}`

- 使用特定的哈希算法对 Phar 文件进行签名：

`phar sign -f {{path/to/phar_file}} -h {{algorithm}}`

- 使用 OpenSSL 私钥对 Phar 文件进行签名：

`phar sign -f {{path/to/phar_file}} -h openssl -y {{path/to/private_key}}`

- 显示帮助和可用的哈希/压缩算法：

`phar help`