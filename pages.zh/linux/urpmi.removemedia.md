# urpmi.removemedia

> 在Mageia中移除媒体。
> 注意：Mageia文档使用medium和repository作为同义词。
> 另见：`urpmi`，`urpme`，`urpmi.addmedia`，`urpmi.update`，`urpmf`，`urpmq`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmi.removemedia>。

- 移除一个媒体：

`sudo urpmi.removemedia {{medium}}`

- 移除所有媒体：

`sudo urpmi.removemedia -a`

- 根据媒体名称模糊匹配移除媒体：

`sudo urpmi.removemedia -y {{keyword}}`