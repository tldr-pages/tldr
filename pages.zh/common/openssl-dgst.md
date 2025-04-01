# openssl dgst

> 用于生成摘要值和执行签名操作的 OpenSSL 命令。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html>.

- 计算文件的 SHA256 摘要，将结果保存到指定文件：

`openssl dgst -sha256 -binary -out {{output_file}} {{input_file}}`

- 使用 RSA 密钥签名文件，将结果保存到指定文件：

`openssl dgst -sign {{private_key_file}} -sha256 -sigopt rsa_padding_mode:pss -out {{output_file}} {{input_file}}`

- 验证 RSA 签名：

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} -sigopt rsa_padding_mode:pss {{signature_message_file}}`

- 使用 ECDSA 密钥签名文件：

`openssl dgst -sign {{private_key_file}} -sha256 -out {{output_file}} {{input_file}}`

- 验证 ECDSA 签名：

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} {{signature_message_file}}`
