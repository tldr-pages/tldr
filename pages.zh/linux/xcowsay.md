# xcowsay

> 在您的 Linux 桌面上显示一头可爱的牛和指定的消息。
> 牛的显示时间是固定的或则是根据文本大小计算得出的。 点击牛即马上关闭。
> 更多信息：<https://www.doof.me.uk/xcowsay/>.

- 显示一头说 “hello, world” 的牛：

`xcowsay "{{hello, world}}"`

- 显示一头牛和消息，该消息是另一个命令的输出：

`ls | xcowsay`

- 显示一头有指定 X 和 Y 坐标的牛：

`xcowsay --at={{X}},{{Y}}`

- 显示一头不同大小的牛：

`xcowsay --cow-size={{small|med|large}}`

- 显示思想泡泡而不是说话泡泡：

`xcowsay --think`

- 用指定的照片来代替默认的牛：

`xcowsay --image={{路径/到/文件}}`
