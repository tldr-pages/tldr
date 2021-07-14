# gpg-zip

> 使用`GPG`加密存档中的文件和目录。
> 更多信息：<https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html>.

- 使用密码将一个目录加密为`archive.gpg`:

`gpg-zip --symmetric --output {{archive.gpg}} {{path/to/directory}}`

- 将`archive.gpg`解密到同名目录中：

`gpg-zip --decrypt {{path/to/archive.gpg}}`

- 列出加密的`archive.gpg`的内容：

`gpg-zip --list-archive {{path/to/archive.gpg}}`
