# net

> ネットワーク関連の設定を表示、変更するためのシステムユーティリティ。
> もっと詳しく: <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>。

- Windowsサービスを同期的に開始または停止する:

`net {{start|stop}} {{サービス}}`

- 現在のコンソールでSMB共有が利用可能であることを確認する:

`net use {{\\smb共有フォルダ}} /USER:{{ユーザ名}}`

- 現在SMBで共有されているフォルダを表示する:

`net share`

- SMB共有の使用者を表示する(管理者特権コンソールで実行):

`net session`

- ローカルセキュリティグループ内のユーザーを表示する:

`net localgroup "{{Administrators}}"`

- ローカルセキュリティグループにユーザーを追加する(管理者特権コンソールで実行):

`net localgroup "{{Administrators}}" {{ユーザ名}} /add`

- サブコマンドのヘルプを表示する:

`net help {{サブコマンド}}`

- ヘルプを表示する:

`net help`
