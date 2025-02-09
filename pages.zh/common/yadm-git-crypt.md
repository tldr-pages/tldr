# yadm git-crypt

> Git Crypt 能够实现 Git 仓库中文件的透明加密和解密。
> 请参阅：`git-crypt`。
> 更多信息：<https://github.com/AGWA/git-crypt>.

- 初始化仓库以使用 Git Crypt：

`yadm git-crypt init`

- 使用 GPG 共享仓库：

`yadm git-crypt add-gpg-user {{用户_id}}`

- 克隆包含加密文件的仓库后，解锁它们：

`yadm git-crypt unlock`

- 导出对称密钥：

`yadm git-crypt export-key {{路径/到/密钥文件}}`
