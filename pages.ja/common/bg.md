# bg

> 一時停止していたジョブ（例. `<Ctrl z>` 使用時）を再開し、バックグラウンドで実行します。
> もっと詳しく: <https://www.gnu.org/software/bash/manual/bash.html#index-bg>。

- 最も最近に一時停止されたジョブを再開し、バックグラウンドで実行する:

`bg`

- 指定されたジョブ（`jobs -l` でジョブIDを取得）を再開し、バックグラウンドで実行する:

`bg %{{ジョブID}}`
