# whatis

> マニュアルページから、一行の説明文を表示します。
> 詳しくはこちら: <https://manned.org/whatis>

- manページの説明文を表示する:

`whatis {{コマンド}}`

- 説明文を行末で切らないで表示する:

`whatis --long {{コマンド}}`

- globパターンにマッチするすべてのコマンドの説明文を表示する:

`whatis --wildcard {{net*}}`

- 正規表現でmanページの説明文を検索する:

`whatis --regex '{{wish[0-9]\.[0-9]}}'`

- 言語を指定して説明文で表示する:

`whatis --locale={{ja}} {{コマンド}}`
