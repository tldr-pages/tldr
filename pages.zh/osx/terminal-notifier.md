# terminal-notifier

> 发送 macOS 用户通知。
> 更多信息：<https://github.com/julienXX/terminal-notifier>。

- 发送通知（只需要消息）：

`terminal-notifier -group {{tldr-info}} -title {{TLDR}} -message '{{TLDR 很棒}}'`

- 使用声音显示管道数据：

`echo '{{管道消息数据！}}' | terminal-notifier -sound {{default}}`

- 当通知被点击时打开 URL：

`terminal-notifier -message '{{检查你的 Apple 股票！}}' -open '{{http://finance.yahoo.com/q?s=AAPL}}'`

- 当通知被点击时打开应用程序：

`terminal-notifier -message '{{已导入 42 个联系人。}}' -activate {{com.apple.AddressBook}}`