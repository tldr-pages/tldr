# gpg

> GNU 隐私保护工具。
> 请参阅 `gpg2` 了解 GNU 隐私保护工具 2。大多数操作系统将 `gpg` 链接到 `gpg2`。
> 更多信息：<https://gnupg.org>。

- 交互式创建 GPG 公钥和私钥：

`gpg --full-generate-key`

- 对 `doc.txt` 进行签名而不加密（输出写入 `doc.txt.asc`）：

`gpg --clearsign {{doc.txt}}`

- 为 alice@example.com 和 bob@example.com 加密并签名 `doc.txt`（输出到 `doc.txt.gpg`）：

`gpg --encrypt --sign --recipient {{alice@example.com}} --recipient {{bob@example.com}} {{doc.txt}}`

- 仅使用密码短语加密 `doc.txt`（输出到 `doc.txt.gpg`）：

`gpg --symmetric {{doc.txt}}`

- 解密 `doc.txt.gpg`（输出到 `stdout`）：

`gpg --decrypt {{doc.txt.gpg}}`

- 导入公钥：

`gpg --import {{public.gpg}}`

- 导出 alice@example.com 的公钥（输出到 `stdout`）：

`gpg --export --armor {{alice@example.com}}`

- 导出 alice@example.com 的私钥（输出到 `stdout`）：

`gpg --export-secret-keys --armor {{alice@example.com}}`