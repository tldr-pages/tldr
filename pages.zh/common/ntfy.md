# ntfy

> 发送和接收 HTTP POST 通知。
> 更多信息：<https://github.com/binwiederhier/ntfy>。

- 向 `security` 主题发送消息：

`ntfy pub security "{{前门已打开。}}"`

- 带有标题、优先级和标签发送：

`ntfy publish --title="{{有人购买了您的商品}}" --priority={{高}} --tags={{鸭子}} {{ebay}} "{{有人刚刚购买了您的商品：鸭嘴兽雕塑}}"`

- 在早上 8:30 发送：

`ntfy pub --at=8:30am {{延迟主题}} "{{该上学了，懒虫...}}"`

- 触发一个 webhook：

`ntfy trigger {{我的_webhook}}`

- 订阅一个主题（按 `<Ctrl c>` 停止监听）：

`ntfy sub {{家庭自动化}}`

- 显示帮助：

`ntfy --help`
