# scrapy

> ウェブクローリングのフレームワークです。
> 詳しくはこちら: <https://scrapy.org>.

- プロジェクトを作成する:

`scrapy startproject {{プロジェクト名}}`

- スパイダーを作成する (プロジェクトのディレクトリ内での実行):

`scrapy genspider {{スパイダー名}} {{ウェブサイトのドメイン名}}`

- スパイダーを編集する (プロジェクトのディレクトリ内での実行):

`scrapy edit {{スパイダー名}}`

- スパイダーを実行する (プロジェクトのディレクトリ内での実行):

`scrapy crawl {{スパイダー名}}`

- Scrapyが見るようにWebページを取得しソースを`stdout`(標準出力)に表示する:

`scrapy fetch {{url}}`

- Scrapyが見ているようにデフォルトブラウザ内でウェブページを開く(より応答に忠実であるようにするためにJavaScriptを無効化している):

`scrapy view {{url}}`

- URL用のScrapyシェルを開き、Python(もしくは可能であればIPython)シェル内でページソースとの対話式でのやり取りを可能にする:

`scrapy shell {{url}}`
