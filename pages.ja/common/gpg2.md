# gpg2

> GNU Privacy Guard 2。
> GNU Privacy Guard 1 については `gpg` を参照してください。
> もっと詳しく: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>。

- インポートされたキーを一覧表示する:

`gpg2 --list-keys`

- 指定したファイルを指定した受信者のために暗号化し、`.gpg`を付加した新しいファイルに出力を書き出す:

`gpg2 --encrypt --recipient {{alice@example.com}} {{path/to/doc.txt}}`

- 指定したファイルをパスフレーズのみで暗号化し、`.gpg`を付加した新しいファイルに出力を書き出す:

`gpg2 --symmetric {{path/to/doc.txt}}`

- 指定したファイルを復号し、結果を`stdout`に出力する:

`gpg2 --decrypt {{path/to/doc.txt.gpg}}`

- 公開鍵をインポートする:

`gpg2 --import {{path/to/public_key.gpg}}`

- 指定したメールアドレスの公開鍵を`stdout`にエクスポートする:

`gpg2 --export --armor {{alice@example.com}}`

- 指定したメールアドレスの秘密鍵を`stdout`にエクスポートする:

`gpg2 --export-secret-keys --armor {{alice@example.com}}`
