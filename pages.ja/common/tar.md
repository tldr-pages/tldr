# tar

> アーカイブ(複数のファイルやフォルダを1つのファイルに纏める)為のユーティリティー。
> gzipやbzip2などの圧縮方法と組み合わせることが多いです。
> 詳しくはこちら: <https://www.gnu.org/software/tar>.

- アーカイブを作成し、それをファイルに書き込む:

`tar cf {{target.tar}} {{file1}} {{file2}} {{file3}}`

- gzip形式で圧縮されたアーカイブを作成し、それをファイルに書き込む:

`tar czf {{target.tar.gz}} {{file1}} {{file2}} {{file3}}`

- 相対パスを用いてディレクトリからgzip形式のアーカイブを作成する:

`tar czf {{target.tar.gz}} --directory={{path/to/directory}} .`

- (圧縮された)アーカイブファイルを現在いるディレクトリに過程を詳細表示して展開する:

`tar xvf {{source.tar[.gz|.bz2|.xz]}}`

- (圧縮された)アーカイブファイルを指定のディレクトリに展開する:

`tar xf {{source.tar[.gz|.bz2|.xz]}} --directory={{directory}}`

- 圧縮されたアーカイブを作成し、それをファイルに書き込む。接尾辞で圧縮プログラムを指定する:

`tar caf {{target.tar.xz}} {{file1}} {{file2}} {{file3}}`

- tarファイルの内容を詳細に表示する:

`tar tvf {{source.tar}}`

- アーカイブファイルからパターンに合致するファイルを抽出する:

`tar xf {{source.tar}} --wildcards "{{*.html}}"`
