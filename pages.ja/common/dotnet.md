# dotnet

> .NET Core 用のクロスプラットフォーム .NET コマンドラインツール。
> `build` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://learn.microsoft.com/dotnet/core/tools>。

- .NET プロジェクトを初期化する:

`dotnet new {{テンプレート短縮名}}`

- NuGet パッケージを復元する:

`dotnet restore`

- 現在のディレクトリで .NET プロジェクトをビルドして実行する:

`dotnet run`

- パッケージ化された dotnet アプリケーションを実行する (必要なのはランタイムだけで、残りのコマンドには.NET Core SDK がインストールされている必要がある):

`dotnet {{path/to/application.dll}}`
