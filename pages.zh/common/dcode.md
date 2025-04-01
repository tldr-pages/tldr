# dcode

> 递归检测和解码字符串，支持十六进制、十进制、二进制、Base64、URL、FromChar 编码、凯撒密码以及 MD5、SHA1 和 SHA2 哈希。
> 警告：对于 MD5、SHA1 和 SHA2 哈希查找，使用第三方网络服务。对于敏感数据，请使用 `-s` 以避免使用这些服务。
> 更多信息：<https://github.com/s0md3v/Decodify>。

- 递归检测和解码一个字符串：

`dcode "{{NjM3YTQyNzQ1YTQ0NGUzMg==}}"`

- 将字符串按指定偏移量旋转：

`dcode -rot {{11}} "{{spwwz hzcwo}}"`

- 将字符串按所有 26 个可能的偏移量旋转：

`dcode -rot {{all}} "{{bpgkta xh qtiitg iwpc sr}}"`

- 反转一个字符串：

`dcode -rev "{{hello world}}"`