# wget

> Webからファイルをダウンロードします。
> HTTP, HTTPS, そして FTP をサポートします。
> もっと詳しく: <https://www.gnu.org/software/wget>。

- URLの内容を、ファイルにダウンロードする (この場合 "foo" と言う名前で):

`wget {{https://example.com/foo}}`

- URLの内容を、ファイルにダウンロードする (この場合 "bar" と言う名前で):

`wget --output-document {{bar}} {{https://example.com/foo}}`

- 1つのウェブページと、その全てのリソースを、リクエスト間隔を3秒にしてダウンロードする (スクリプト、スタイルシート、画像など):

`wget --page-requisites --convert-links --wait=3 {{https://example.com/somepage.html}}`

- ディレクトリと、そのサブディレクトリ内のリストされたファイルを、全てダウンロードする (埋め込まれたページ要素はダウンロードしない):

`wget --mirror --no-parent {{https://example.com/somepath/}}`

- ダウンロード速度と接続再試行回数を制限する:

`wget --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}`

- HTTPサーバーからBasic認証を使って、ファイルをダウンロードする (FTPも機能する):

`wget --user={{ユーザ名}} --password={{パスワード}} {{https://example.com}}`

- 未完了のダウンロードを続行する:

`wget --continue {{https://example.com}}`

- テキストファイルに格納されている全てのURLを、特定のディレクトリにダウンロードする:

`wget --directory-prefix {{path/to/directory}} --input-file {{URLs.txt}}`
