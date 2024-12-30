# qr

> 在终端中使用 ANSI VT-100 转义码生成 QR 码。
> 更多信息：<https://github.com/lincolnloop/python-qrcode/>.

- 生成 QR 码：

`echo "{{data}}" | qr`

- 指定错误纠正级别（默认为 M）：

`echo "{{data}}" | qr --error-correction={{L|M|Q|H}}`