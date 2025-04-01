# xidel

> 从 HTML/XML 页面和 JSON API 下载并提取数据。
> 更多信息：<https://www.videlibri.de/xidel.html>。

- 打印通过 Google 搜索找到的所有 URL：

`xidel {{https://www.google.com/search?q=test}} --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"`

- 打印通过 Google 搜索找到的所有页面的标题并下载这些页面：

`xidel {{https://www.google.com/search?q=test}} --follow "{{//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']}}" --extract {{//title}} --download {{'{$host}/'}}`

- 跟踪页面上的所有链接并打印页面标题，使用 XPath：

`xidel {{https://example.org}} --follow {{//a}} --extract {{//title}}`

- 跟踪页面上的所有链接并打印页面标题，使用 CSS 选择器：

`xidel {{https://example.org}} --follow "{{css('a')}}" --css {{title}}`

- 跟踪页面上的所有链接并打印页面标题，使用模式匹配：

`xidel {{https://example.org}} --follow "{{<a>{.}</a>*}}" --extract "{{<title>{.}</title>}}"`

- 从 example.xml 中读取模式（同时检查包含 "ood" 的元素是否存在，否则将失败）：

`xidel {{path/to/example.xml}} --extract "{{<x><foo>ood</foo><bar>{.}</bar></x>}}"`

- 使用模式匹配从 Stack Overflow 的 RSS 源打印所有最新的问题及其标题和 URL：

`xidel {{http://stackoverflow.com/feeds}} --extract "{{<entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+}}"`

- 检查 Reddit 上的未读邮件，结合使用 CSS、XPath、JSONiq 和自动表单评估进行网页抓取：

`xidel {{https://reddit.com}} --follow "{{form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})}}" --extract "{{css('#mail')/@title}}"`
