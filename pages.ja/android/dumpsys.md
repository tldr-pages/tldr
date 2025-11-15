# dumpsys

> Android システムサービスの情報を取得します。
> このコマンドは `adb shell` 経由でのみ実行できます。
> もっと詳しく: <https://developer.android.com/tools/dumpsys>。

- すべてのシステムに対して診断を出力します:

`dumpsys`

- 特定のシステムに対して診断を出力します:

`dumpsys {{service}}`

- `dumpsys` で表示できるすべてのサービスの情報を表示します:

`dumpsys -l`

- 指定したサービスを引数をサービスに表示させます:

`dumpsys {{service}} -h`

- 指定したサービスを診断から除外して出力します:

`dumpsys --skip {{service}}`

- タイムアウトを秒数で指定します。(デフォルトは10秒):

`dumpsys -t {{8}}`
