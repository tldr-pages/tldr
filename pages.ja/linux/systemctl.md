# systemctl

> systemd システムとサービスマネージャーを制御します。
> もっと詳しく: <https://www.freedesktop.org/software/systemd/man/systemctl.html>。

- 実行中のサービスを全て表示する:

`systemctl status`

- 失敗状態のユニット一覧:

`systemctl --failed`

- サービスを Start/Stop/Restart/Reload/Show 状態にする:

`systemctl {{start|stop|restart|reload|status}} {{ユニット}}`

- 起動時に起動するユニットを Enable/Disable に設定する:

`systemctl {{enable|disable}} {{ユニット}}`

- systemdを再読み込みし、新規または変更されたユニットをスキャンする:

`systemctl daemon-reload`

- ユニットが active/enabled/failed かをチェックする:

`systemctl {{is-active|is-enabled|is-failed}} {{ユニット}}`

- 全ての service/socket/automount ユニットを running/failed 状態でフィルタリングして一覧表示する:

`systemctl list-units {{[-t|--type]}} {{service|socket|automount}} --state {{failed|running}}`

- ユニットファイルの内容と絶対パスを表示する:

`systemctl cat {{ユニット}}`
