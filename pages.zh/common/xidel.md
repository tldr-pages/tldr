# xidel

> 从HTML/XML页面以及JSON API下载和提取数据。
> 更多信息：<https://www.videlibri.de/xidel.html>。

- 打印通过Google搜索找到的所有URL：

`xidel {{https://www.google.com/search?q=test}} --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"`

- 打印通过Google搜索找到的所有页面的标题并下载它们：

`xidel {{https://www.google.com/search?q=test}} --follow "{{//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']}}" --extract {{//title}} --download {{'{$host}/'}}`

- 跟随页面上的所有链接并打印标题，使用XPath：

`xidel {{https://example.org}} --follow {{//a}} --extract {{//title}}`

- 跟随页面上的所有链接并打印标题，使用CSS选择器：

`xidel {{https://example.org}} --follow "{{css('a')}}" --css {{title}}`

- 跟随页面上的所有链接并打印标题，使用模式匹配：

`xidel {{https://example.org}} --follow "{{<a>{.}</a>*}}" --extract "{{<title>{.}</title>}}"`

- 从example.xml读取模式（这也将检查是否存在包含"ood"的元素，如果没有则失败）：

`xidel {{path/to/example.xml}} --extract "{{<x><foo>ood</foo><bar>{.}</bar></x>}}"`

- 使用模式匹配打印所有最新的Stack Overflow问题的标题和URL，通过他们的RSS源：

`xidel {{http://stackoverflow.com/feeds}} --extract "{{<entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+}}"`

- 检查未读的Reddit邮件，网络抓取，结合CSS、XPath、JSONiq，并自动进行表单评估：

`xidel {{https://reddit.com}} --follow "{{form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})}}" --extract "{{css('#mail')/@title}}"`