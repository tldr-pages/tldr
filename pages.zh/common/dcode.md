# dcode

> 递归检测和解码字符串，支持十六进制、十进制、二进制、base64、URL、FromChar 编码、凯撒密码，以及 MD5、SHA1 和 SHA2 哈希。
> 警告：使用第三方网络服务进行 MD5、SHA1 和 SHA2 哈希查找。对于敏感数据，请使用 `-s` 来避免使用这些服务。
> 更多信息：<https://github.com/s0md3v/Decodify>。

- 递归检测和解码一个字符串：

`dcode "{{NjM3YTQyNzQ1YTQ0NGUzMg==}}"`

- 按指定偏移量旋转字符串：

`dcode -rot {{11}} "{{spwwz hzcwo}}"`

- 按所有 26 种可能的偏移量旋转字符串：

`dcode -rot {{all}} "{{bpgkta xh qtiitg iwpc sr}}"`

- 反转一个字符串：

`dcode -rev "{{hello world}}"`