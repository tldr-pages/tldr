# gpg

> GNU Privacy Guard.
> 请参阅`gpg2`了解 GNU Privacy Guard 2.
> 更多信息：<https://gnupg.org>.

- 不加密，仅对`doc.txt`进行签名（生成`doc.txt.asc`，格式为 ASCII 码形式）：

`gpg --clearsign {{doc.txt}}`

- 对`doc.txt`进行签名并加密（生成`doc.txt.asc`，格式为 ASCII 码形式）：

`gpg --local-user {{sender_id}} --recipient {{recipient_id}} --armor --sign --encrypt {{doc.txt}}`

- 为接收者 alice@example.com 加密`doc.txt`（生成`doc.txt.gpg`）：

`gpg --encrypt --recipient {{alice@example.com}} {{doc.txt}}`

- 只用密码加密`doc.txt`（生成`doc.txt.gpg`）：

`gpg --symmetric {{doc.txt}}`

- 解密`doc.txt.gpg`（输出到标准输出）：

`gpg --decrypt {{doc.txt.gpg}}`

- 导入一个公钥：

`gpg --import {{public.gpg}}`

- 导出 alice@example.com 的公钥（输出到标准输出）：

`gpg --export --armor {{alice@example.com}}`

- 导出 alice@example.com 的私钥（输出到标准输出）：

`gpg --export-secret-keys --armor {{alice@example.com}}`
