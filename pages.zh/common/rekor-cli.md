# rekor-cli

> 软件供应链中生成的元数据的不可变篡改抗性账本。
> 更多信息：<https://github.com/sigstore/rekor>.

- 上传工件到 Rekor:

`rekor-cli upload --artifact {{path/to/file.ext}} --signature {{path/to/file.ext.sig}} --pki-format={{x509}} --public-key={{path/to/key.pub}}`

- 获取透明日志中的条目信息:

`rekor-cli get --uuid={{0e81b4d9299e2609e45b5c453a4c0e7820ac74e02c4935a8b830d104632fd2d1}}`

- 通过工件搜索 Rekor 索引以查找条目:

`rekor-cli search --artifact {{path/to/file.ext}}`

- 通过特定哈希搜索 Rekor 索引以查找条目:

`rekor-cli search --sha {{6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b}}`
