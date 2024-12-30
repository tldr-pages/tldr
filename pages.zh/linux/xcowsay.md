# xcowsay

> 在你的Linux桌面上显示一只可爱的牛和消息。
> 牛会在固定的时间内显示，或者根据文本的大小计算出显示时间。点击牛可以立即关闭它。
> 更多信息：<https://www.doof.me.uk/xcowsay/>.

- 显示一只说“hello, world”的牛：

`xcowsay "{{hello, world}}"`

- 显示一只与其他命令输出的牛：

`ls | xcowsay`

- 在指定的X和Y坐标显示一只牛：

`xcowsay --at={{X}},{{Y}}`

- 显示不同大小的牛：

`xcowsay --cow-size={{small|med|large}}`

- 显示一个思想气泡而不是说话气泡：

`xcowsay --think`

- 显示一张不同的图像而不是默认的牛：

`xcowsay --image={{path/to/file}}`