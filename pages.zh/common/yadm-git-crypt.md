# yadm git-crypt

> Git Crypt 允许在 git 存储库中透明地加密和解密文件。
> 另请参见：`git-crypt`。
> 更多信息：<https://github.com/AGWA/git-crypt>。

- 初始化仓库以使用 Git Crypt：

`yadm git-crypt init`

- 使用 GPG 共享存储库：

`yadm git-crypt add-gpg-user {{user_id}}`

- 克隆带有加密文件的存储库后，解锁它们：

`yadm git-crypt unlock`

- 导出对称密钥：

`yadm git-crypt export-key {{path/to/key_file}}`