# tmux

> 端末のマルチプレクサ。
> ウィンドウやペインなどによる複数セッションを可能にします。
> 参照: `zellij`, `screen`。
> 詳細情報: <https://github.com/tmux/tmux>。

- 新規セッションの開始:

`tmux`

- 新しい名前付きセッションを開始する:

`tmux {{[new|new-session]}} -s {{セッション名}}`

- 既存のセッションを一覧表示:

`tmux {{[ls|list-sessions]}}`

- 直近に使用したセッションにアタッチ:

`tmux {{[a|attach]}}`

- 現在のセッションからの切り離し（tmuxセッション内）:

`<Ctrl b><d>`

- 新しいウィンドウを作成する（tmuxセッション内）:

`<Ctrl b><c>`

- セッションとウィンドウの切り替え（tmuxセッション内）:

`<Ctrl b><w>`

- 名前を指定してセッションを終了させる:

`tmux kill-session -t {{セッション名}}`
