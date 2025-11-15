# zint

> 生成条形码和二维码。
> 更多信息：<https://www.zint.org.uk/manual/chapter/4>.

- 生成一个条形码并保存：

`zint --data "{{UTF-8 数据}}" --output {{路径/到/文件}}`

- 指定生成的编码类型：

`zint --barcode {{编码类型}} --data "{{UTF-8 数据}}" --output {{路径/到/文件}}`

- 列出所有支持的编码类型：

`zint --types`
