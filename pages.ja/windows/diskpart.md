# diskpart

> ディスク、ボリューム、およびパーティションマネージャ。
> 詳細情報: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>。

- 管理者コマンドプロンプトでdiskpartを単独で実行し、コマンドラインを入力する:

`diskpart`

- [対話的] 全てのディスクを一覧表示する:

`list disk`

- [対話的] ボリュームを選択:

`select volume {{ボリューム}}`

- [対話的] 選択したボリュームにドライブレターを割り当てる:

`assign letter {{ドライブレター}}`

- [対話的] 新しいパーティションを作成:

`create partition primary`

- [対話的] 選択したボリュームを有効化:

`active`

- [対話的] diskpartを終了する:

`exit`
