# rekor-cli

> 一种不可变的防篡改元数据账本，生成于软件项目的供应链中。
> 更多信息：<https://github.com/sigstore/rekor>。

- 上传一个工件到 Rekor：

`rekor-cli upload --artifact {{path/to/file.ext}} --signature {{path/to/file.ext.sig}} --pki-format={{x509}} --public-key={{path/to/key.pub}}`

- 获取透明日志中条目的信息：

`rekor-cli get --uuid={{0e81b4d9299e2609e45b5c453a4c0e7820ac74e02c4935a8b830d104632fd2d1}}`

- 根据工件在 Rekor 索引中查找条目：

`rekor-cli search --artifact {{path/to/file.ext}}`

- 根据特定哈希在 Rekor 索引中查找条目：

`rekor-cli search --sha {{6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b}}`