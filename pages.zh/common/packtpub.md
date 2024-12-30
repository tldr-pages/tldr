# packtpub

> 从 packtpub.com 下载免费提供的书籍。
> 更多信息：<https://github.com/vladimyr/packtpub-cli>。

- 以指定的书籍格式（默认为 `pdf`）将每日优惠书籍下载到当前目录：

`packtpub download --type {{pdf|ebup|mobi}}`

- 将每日优惠书籍下载到指定目录：

`packtpub download --dir {{path/to/directory}}`

- 开始与 packtpub.com 的交互式登录：

`packtpub login`

- 从 packtpub.com 登出：

`packtpub logout`

- 显示每日优惠：

`packtpub view-offer`

- 在默认网页浏览器中打开每日优惠：

`packtpub view-offer`

- 显示当前登录的用户：

`packtpub whoami`