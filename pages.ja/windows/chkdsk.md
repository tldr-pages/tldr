# chkdsk

> ファイルシステムとボリュームのメタデータにエラーがないかチェックします。
> もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>。

- チェックするドライブ文字(コロンの後に続く)、マウントポイント、またはボリューム名を指定する:

`chkdsk {{ボリューム名}}`

- 特定のボリュームのエラーを修正する:

`chkdsk {{ボリューム名}} /f`

- チェックする前に指定ボリュームをマウント解除する:

`chkdsk {{ボリューム名}} /x`

- ログファイルのサイズを指定したサイズに変更する (NTFS の場合のみ):

`chkdsk /l{{サイズ数}}`
