# pm

> Android デバイスに関連するアプリケーションの情報を表示します。
> もっと詳しく: <https://developer.android.com/tools/adb#pm>。

- インストールされたすべてのアプリケーションを表示します:

`pm list packages`

- インストールされたすべてのシステムアプリケーションを表示します:

`pm list packages -s`

- インストールされたすべてのサードパーティ製アプリケーションを表示します:

`pm list packages -3`

- 指定したキーワードにマッチするアプリケーションを表示します:

`pm list packages {{keyword1 keyword2 ...}}`

- 指定したアプリケーションのAPKのパスを表示します:

`pm path {{app}}`
