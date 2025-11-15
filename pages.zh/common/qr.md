# qr

> 在终端中使用 ANSI VT-100 转义代码生成二维码。
> 更多信息：<https://manned.org/qr>.

- 生成一个二维码：

`echo "{{数据}}" | qr`

- 指定错误纠正等级（默认为 M）：

`echo "{{数据}}" | qr --error-correction={{L|M|Q|H}}`
