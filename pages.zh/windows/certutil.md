# certutil

> 这是一个用于管理和配置证书信息的工具。
> 更多信息请访问：<https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>。

- 转储配置文件或信息：

`certutil {{filename}}`

- 以十六进制编码文件：

`certutil -encodehex {{path\to\input_file}} {{path\to\output_file}}`

- 将文件编码为Base64：

`certutil -encode {{path\to\input_file}} {{path\to\output_file}}`

- 解码Base64编码的文件：

`certutil -decode {{path\to\input_file}} {{path\to\output_file}}`

- 生成并显示文件的加密哈希值：

`certutil -hashfile {{path\to\input_file}} {{md2|md4|md5|sha1|sha256|sha384|sha512}}`