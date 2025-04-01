# sm

> 全屏显示简短消息。
> 更多信息：<https://github.com/nomeata/screen-message>.

- 全屏显示一条消息：

`sm "{{Hello World!}}"`

- 使用反色显示一条消息：

`sm -i "{{Hello World!}}"`

- 使用自定义前景色显示一条消息：

`sm -f {{blue}} "{{Hello World!}}"`

- 使用自定义背景色显示一条消息：

`sm -b {{#008888}} "{{Hello World!}}"`

- 逆时针旋转 3 次（每次 90 度）显示一条消息：

`sm -r {{3}} "{{Hello World!}}"`

- 使用其他命令的输出显示一条消息：

`{{echo "Hello World!"}} | sm -`