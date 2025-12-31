# gradle

> オープンソースのビルド自動化システムです。
> もっと詳しく: <https://manned.org/gradle>。

- パッケージをコンパイルする:

`gradle build`

- test タスクを除外する:

`gradle build -x {{test}}`

- ビルド中に Gradle がネットワークにアクセスしないようにオフラインモードで実行する:

`gradle build --offline`

- ビルドディレクトリを消去する:

`gradle clean`

- release モードで Android パッケージ (APK) をビルドする:

`gradle assembleRelease`

- 主なタスクを一覧表示する:

`gradle tasks`

- 全てのタスクを一覧表示する:

`gradle tasks --all`
