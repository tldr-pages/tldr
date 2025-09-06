# gpg

> GNU Privacy Guard.
> 更多信息：<https://gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html>.

- 交互地创建 GPG 公钥和私钥：

`gpg {{[--full-gen-key|--full-generate-key]}}`

- 不加密，仅对 `doc.txt` 进行签名（生成 `doc.txt.asc`，格式为 ASCII 码形式）：

`gpg --clearsign {{doc.txt}}`

- 为接收者 alice@example.com 和 bob@example.com 签名并加密 `doc.txt`（生成 `doc.txt.gpg`）：

`gpg {{[-es|--encrypt --sign]}} {{[-r|--recipient]}} {{alice@example.com}} {{[-r|--recipient]}} {{bob@example.com}} {{doc.txt}}`

- 只用密码加密 `doc.txt`（生成 `doc.txt.gpg`）：

`gpg {{[-c|--symmetric]}} {{doc.txt}}`

- 解密 `doc.txt.gpg`（输出到标准输出）：

`gpg {{[-d|--decrypt]}} {{doc.txt.gpg}}`

- 导入一个公钥：

`gpg --import {{public.gpg}}`

- 导出 alice@example.com 的公钥（输出到标准输出）：

`gpg --export {{[-a|--armor]}} {{alice@example.com}}`

- 导出 alice@example.com 的私钥（输出到标准输出）：

`gpg --export-secret-keys {{[-a|--armor]}} {{alice@example.com}}`
