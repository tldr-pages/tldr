# logcat

> エラー時に発生したスタックトレースを含む、アプリケーションによって作成されたログや、システムメッセージのログを削除します。
> もっと詳しく: <https://developer.android.com/tools/logcat>。

- システムログを表示します:

`logcat`

- 指定したファイルにシステムログを書き出します:

`logcat -f {{path/to/file}}`

- 正規表現にマッチする行を表示します:

`logcat --regex {{regular_expression}}`

- 指定したPIDのログを表示します:

`logcat --pid {{pid}}`

- 特定のパッケージのプロセスのログを表示します:

`logcat --pid $(pidof -s {{package}})`
