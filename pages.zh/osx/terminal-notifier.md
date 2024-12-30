# terminal-notifier

> 发送 macOS 用户通知。
> 更多信息请访问：<https://github.com/julienXX/terminal-notifier>。

- 发送通知（只需消息）：

`terminal-notifier -group {{tldr-info}} -title {{TLDR}} -message '{{TLDR 很棒}}'`

- 显示带声音的管道数据：

`echo '{{管道消息数据！}}' | terminal-notifier -sound {{default}}`

- 点击通知时打开 URL：

`terminal-notifier -message '{{查看你的苹果股票！}}' -open '{{http://finance.yahoo.com/q?s=AAPL}}'`

- 点击通知时打开应用程序：

`terminal-notifier -message '{{已导入 42 个联系人。}}' -activate {{com.apple.AddressBook}}`