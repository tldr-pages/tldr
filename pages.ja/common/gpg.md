# gpg

> GNU Privacy Guard。
> もっと詳しく: <https://gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html>。

- GPGの公開鍵と秘密鍵を対話的に作成する:

`gpg {{[--full-gen-key|--full-generate-key]}}`

- 暗号化せずに `doc.txt` に署名する (出力を `doc.txt.asc` に書き出す):

`gpg --clearsign {{doc.txt}}`

- alice@example.com と bob@example.com の `doc.txt` を暗号化して署名する (`doc.txt.gpg` に出力):

`gpg {{[-es|--encrypt --sign]}} {{[-r|--recipient]}} {{alice@example.com}} {{[-r|--recipient]}} {{bob@example.com}} {{doc.txt}}`

- パスフレーズのみで `doc.txt` を暗号化する (`doc.txt.gpg` に出力):

`gpg {{[-c|--symmetric]}} {{doc.txt}}`

- `doc.txt.gpg` を復号化する (`stdout` に出力):

`gpg {{[-d|--decrypt]}} {{doc.txt.gpg}}`

- 公開鍵をインポートする:

`gpg --import {{public.gpg}}`

- alice@example.com 用に公開鍵をエクスポートする (`stdout` に出力):

`gpg --export {{[-a|--armor]}} {{alice@example.com}}`

- alice@example.com の秘密鍵をエクスポートする (`stdout` に出力):

`gpg --export-secret-keys {{[-a|--armor]}} {{alice@example.com}}`
