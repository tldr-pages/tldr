# gcloud kms decrypt

> 使用 Cloud KMS 密钥解密密文文件。
> 相关命令：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/kms/decrypt>。

- 使用指定的密钥、密钥环和位置解密文件：

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{global}} --ciphertext-file={{path/to/ciphertext}} --plaintext-file={{path/to/plaintext}}`

- 使用额外的认证数据 (AAD) 解密文件，并将解密的明文写入 `stdout`：

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{global}} --additional-authenticated-data-file={{path/to/file.aad}} --ciphertext-file={{path/to/ciphertext}} --plaintext-file=-`
