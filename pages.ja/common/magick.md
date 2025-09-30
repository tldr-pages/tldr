# magick

> 画像フォーマットの作成、編集、合成、変換を行います。
> このツールは、ImageMagick 7+ の `convert` を置き換えるものです。古いツールを version 7+ で使うには、 `magick convert` を参照してください。
> `mogrify` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://imagemagick.org>。

- 画像フォーマットを変換する:

`magick {{path/to/input_image.png}} {{path/to/output_image.jpg}}`

- 入力画像をリサイズし、新規に出力する:

`magick {{path/to/input_image.jpg}} -resize {{100x100}} {{path/to/output_image.jpg}}`

- 現在のディレクトリにある全ての JPEG 画像から GIF を作成:

`magick {{*.jpg}} {{path/to/images.gif}}`

- 市松模様(チェッカーボード)の画像を生成する:

`magick -size {{640x480}} pattern:checkerboard {{path/to/checkerboard.png}}`

- 現在のディレクトリ内の全ての JPEG 画像から PDF ファイルを作成する:

`magick {{*.jpg}} -adjoin {{path/to/file.pdf}}`
