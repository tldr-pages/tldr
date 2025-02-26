# ssh-keygen

> 認証やパスワード不要のログインなどに使われるSSHキーを生成します。
> もっと詳しく: <https://man.openbsd.org/ssh-keygen>。

- 対話的にキーを生成します:

`ssh-keygen`

- 32ラウンド回数の鍵導出関数でed25519鍵を生成し、特定のファイルに保存する:

`ssh-keygen -t {{ed25519}} -a {{32}} -f {{~/.ssh/filename}}`

- Eメールをコメントとして、RSA 4096ビット鍵を生成する:

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{comment|email}}"`

- known_hostsファイルからホストの鍵を削除する (既知のホストが新しい鍵を持つ場合に便利):

`ssh-keygen -R {{remote_host}}`

- 鍵のフィンガープリントをMD5 Hexで取得する:

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/filename}}`

- 鍵のパスワードを変更する:

`ssh-keygen -p -f {{~/.ssh/filename}}`

- 鍵の形式を変更する (たとえば OPENSSH 形式から PEM 形式へ):

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/OpenSSH_private_key}}`

- 秘密鍵から公開鍵を取得する:

`ssh-keygen -y -f {{~/.ssh/OpenSSH_private_key}}`
