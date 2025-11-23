# wget

> Webからファイルをダウンロードします。
> HTTP, HTTPS, そして FTP をサポートします。
> もっと詳しく: <https://www.gnu.org/software/wget/manual/wget.html>。

- URLの内容を、ファイルにダウンロードする (この場合 "foo" と言う名前で):

`wget {{https://example.com/foo}}`

- URLの内容を、ファイルにダウンロードする (この場合 "bar" と言う名前で):

`wget {{[-O|--output-document]}} {{bar}} {{https://example.com/foo}}`

- 1つのウェブページと、その全てのリソースを、リクエスト間隔を3秒にしてダウンロードする (スクリプト、スタイルシート、画像など):

`wget {{[-p|--page-requisites]}} {{[-k|--convert-links]}} {{[-w|--wait]}} 3 {{https://example.com/somepage.html}}`

- ディレクトリと、そのサブディレクトリ内のリストされたファイルを、全てダウンロードする (埋め込まれたページ要素はダウンロードしない):

`wget {{[-m|--mirror]}} {{[-np|--no-parent]}} {{https://example.com/somepath/}}`

- ダウンロード速度と接続再試行回数を制限する:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/somepath/}}`

- HTTPサーバーからBasic認証を使って、ファイルをダウンロードする (FTPも機能する):

`wget --user {{ユーザ名}} --password {{パスワード}} {{https://example.com}}`

- 未完了のダウンロードを続行する:

`wget {{[-c|--continue]}} {{https://example.com}}`

- テキストファイルに格納されている全てのURLを、特定のディレクトリにダウンロードする:

`wget {{[-P|--directory-prefix]}} {{path/to/directory}} {{[-i|--input-file]}} {{URLs.txt}}`
