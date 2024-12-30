# tlmgr 密钥

> 管理用于验证 TeX Live 数据库的 GPG 密钥。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出所有 TeX Live 密钥：

`tlmgr key list`

- 从特定文件添加密钥：

`sudo tlmgr key add {{path/to/key.gpg}}`

- 从 `stdin` 添加密钥：

`cat {{path/to/key.gpg}} | sudo tlmgr key add -`

- 根据 ID 删除特定密钥：

`sudo tlmgr key remove {{key_id}}`