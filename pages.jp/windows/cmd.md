# cmd

> Windowsコマンドインタープリター。
> 詳しくはこちら: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>

- コマンドインタープリターの新しいインスタンスを開始します:

`cmd`

- 指定されたコマンドを実行して終了します:

`cmd /c {{コマンド}}`

- 指定されたコマンドを実行して、インタラクティブシェルに入ります:

`cmd /k {{コマンド}}`

- コマンドの出力での「echo」の使用を無効にします:

`cmd /q`

- 環境変数の拡張を有効または無効にします:

`cmd /v:{{on|off}}`

- コマンド拡張機能を有効または無効にします:

`cmd /e:{{on|off}}`

- 出力でUnicodeエンコーディングを使用するように強制します:

`cmd /u`
