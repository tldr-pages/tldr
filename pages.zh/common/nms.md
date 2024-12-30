# nms

> 命令行工具，可以重现1992年电影《Sneakers》中著名的数据解密效果，来自`stdin`。
> 更多信息请访问：<https://github.com/bartobri/no-more-secrets>。

- 在按下按键后解密文本：

`echo "{{Hello, World!}}" | nms`

- 立即解密输出，无需等待按键：

`{{ls -la}} | nms -a`

- 解密文件内容，并自定义输出颜色：

`cat {{path/to/file}} | nms -a -f {{blue|white|yellow|black|magenta|green|red}}`

- 在解密之前清屏：

`{{command}} | nms -a -c`