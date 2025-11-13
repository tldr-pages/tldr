# alias

> alias （コマンド文字列を置き換える別名）を作成します。
> alias は `~/.bashrc` などの shell の設定ファイルで定義されない限り、現在のセッションで失効します。
> もっと詳しく: <https://www.gnu.org/software/bash/manual/bash.html#index-alias>。

- alias の一覧表示:

`alias`

- alias を作成する:

`alias {{別名}}="{{コマンド}}"`

- 指定した alias に紐付くコマンドの表示:

`alias {{別名}}`

- 作成された alias の削除:

`unalias {{別名}}`

- `rm` を対話型にする:

`alias {{rm}}="{{rm -i}}"`

- `ls -a` のショートカットして `la` を作成する:

`alias {{la}}="{{ls -a}}"`
