# ntfy

> 发送和接收 HTTP POST 通知。
> 更多信息：<https://github.com/binwiederhier/ntfy>。

- 发送消息到 `security` 主题：

`ntfy pub security "{{前门已经打开。}}"`

- 带标题、优先级和标签发送：

`ntfy publish --title="{{有人购买了你的商品}}" --priority={{high}} --tags={{duck}} {{ebay}} "{{有人刚刚购买了你的商品：鸭嘴兽雕塑}}"`

- 在早上 8:30 发送：

`ntfy pub --at=8:30am {{delayed_topic}} "{{该上学了，睡美人...}}"`

- 触发一个 webhook：

`ntfy trigger {{my_webhook}}`

- 订阅一个主题 (按 Ctrl-C 停止监听)：

`ntfy sub {{home_automation}}`

- 显示帮助：

`ntfy --help`