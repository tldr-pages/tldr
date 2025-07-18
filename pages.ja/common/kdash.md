# kdash

> ターミナル上でKubernetesのダッシュボードを作成するためのコマンドラインインターフェイス。
> もっと詳しく: <https://github.com/kdash-rs/kdash/>。

- ダッシュボードの起動:

`kdash`

- デバッグモードで起動しログをファイルに書き込む:

`kdash {{[-d|--debug]}}`

- ティックレートを設定する:

`kdash {{[-t|--tick-rate]}} {{100}}`

- ポーリングレートを設定する:

`kdash -t {{200}} -p {{400}}`
