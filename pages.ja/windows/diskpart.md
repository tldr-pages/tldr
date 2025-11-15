# diskpart

> ディスク、ボリューム、およびパーティションマネージャ。
> もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>。

- 管理者コマンドプロンプトでdiskpartを単独で実行し、コマンドラインを入力する:

`diskpart`

- 全てのディスクを一覧表示する:

`list disk`

- ボリュームを選択:

`select volume {{ボリューム}}`

- 選択したボリュームにドライブレターを割り当てる:

`assign letter {{ドライブレター}}`

- 新しいパーティションを作成:

`create partition primary`

- 選択したボリュームを有効化:

`active`

- diskpartを終了する:

`exit`
