# cowsay

> 打印 ASCII 艺术（默认是一头牛）说或想些什么。
> 更多信息：<https://github.com/tnalpgge/rank-amateur-cowsay>。

- 打印一头 ASCII 牛，说“hello, world”：

`cowsay "{{hello, world}}"`

- 从 `stdin` 打印 ASCII 牛说的内容：

`echo "{{hello, world}}" | cowsay`

- 列出所有可用的 ASCII 艺术类型：

`cowsay -l`

- 打印指定的 ASCII 艺术，说“hello, world”：

`cowsay -f {{art}} "{{hello, world}}"`

- 打印一头想“我只是一头牛，不是思想家……”的 ASCII 死牛：

`cowthink -d "{{I'm just a cow, not a great thinker...}}"`

- 打印带有自定义眼睛的 ASCII 牛，说“hello, world”：

`cowsay -e {{characters}} "{{hello, world}}"`