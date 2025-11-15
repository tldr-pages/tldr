# iw

> ワイヤレスデバイスの表示と操作を行います。
> `iw dev` も参照してください。
> もっと詳しく: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>。

- 利用可能なワイヤレスネットワークをスキャンする:

`iw dev {{wlp}} scan`

- 開いているワイヤレスネットワークに接続する:

`iw dev {{wlp}} connect {{SSID}}`

- 現在の接続を切断する:

`iw dev {{wlp}} disconnect`

- 現在の接続に関する情報を表示:

`iw dev {{wlp}} link`

- 全ての物理・論理ワイヤレスネットワークインターフェースを一覧表示:

`iw dev`

- 全ての物理ハードウェアインターフェースの、全てのワイヤレス機能を一覧表示:

`iw phy`

- カーネルの現在のワイヤレス規制ドメイン情報を一覧表示:

`iw reg get`

- 全てのコマンドのヘルプを表示:

`iw help`
