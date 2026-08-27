# age

> 一個簡潔、現代且安全的檔案加密工具。
> 另請參閱：`age-keygen`、`age-inspect`。
> 更多資訊：<https://github.com/FiloSottile/age#usage>。

- 產生可使用密碼片語解密的加密檔案：

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{path/to/encrypted_file.age}} {{path/to/unencrypted_file}}`

- 使用直接輸入的一個或多個公開金鑰加密檔案（重複使用 `--recipient` 旗標以指定多個公開金鑰）：

`age {{[-r|--recipient]}} {{public_key}} {{[-o|--output]}} {{path/to/encrypted_file.age}} {{path/to/unencrypted_file}}`

- 使用檔案中指定的公開金鑰為一個或多個收件者加密檔案（每行一個金鑰）：

`age {{[-R|--recipients-file]}} {{path/to/recipients_file.txt}} {{[-o|--output]}} {{path/to/encrypted_file.age}} {{path/to/unencrypted_file}}`

- 使用密碼片語解密檔案：

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{path/to/decrypted_file}} {{path/to/encrypted_file.age}}`

- 使用私密金鑰檔案解密檔案：

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{path/to/private_key_file}} {{[-o|--output]}} {{path/to/decrypted_file}} {{path/to/encrypted_file.age}}`
