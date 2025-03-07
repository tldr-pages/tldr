# msbuild

> Microsoft の Visual Studio プロジェクトソリューション用ビルドツールです。
> もっと詳しく: <https://learn.microsoft.com/visualstudio/msbuild>。

- 現在のディレクトリにある最初のプロジェクトファイルをビルドする:

`msbuild`

- 特定のプロジェクトファイルをビルドする:

`msbuild {{path/to/project_file}}`

- ビルドするターゲットを 1 つ以上指定する (セミコロン(;)で区切る):

`msbuild {{path/to/project_file}} /target:{{ターゲット名}}`

- プロパティを 1 つ以上指定する (セミコロン(;)で区切る):

`msbuild {{path/to/project_file}} /property:{{プロパティ名=値}}`

- 使用するビルドツールのバージョンを指定する:

`msbuild {{path/to/project_file}} /toolsversion:{{バージョン}}`

- プロジェクトの設定方法に関する詳細情報をログの最後に表示する:

`msbuild {{path/to/project_file}} /detailedsummary`

- ヘルプを表示:

`msbuild /help`
