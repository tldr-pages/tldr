# tlmgr key

> 管理用于验证 TeX Live 数据库的 GPG 密钥。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出 TeX Live 的所有密钥：

`tlmgr key list`

- 从特定文件中添加密钥：

`sudo tlmgr key add {{path/to/key.gpg}}`

- 从 `stdin` 添加密钥：

`cat {{path/to/key.gpg}} | sudo tlmgr key add -`

- 通过其 ID 移除特定密钥：

`sudo tlmgr key remove {{key_id}}`
