# mumble

> 低延迟、高质量的语音聊天软件。
> 更多信息：<https://www.mumble.info>。

- 打开 Mumble：

`mumble`

- 打开 Mumble 并立即连接到服务器：

`mumble mumble://{{username}}@{{example.com}}`

- 打开 Mumble 并立即连接到需要密码的服务器：

`mumble mumble://{{username}}:{{password}}@{{example.com}}`

- 在运行中的 Mumble 实例中静音/取消静音麦克风：

`mumble rpc {{mute|unmute}}`

- 静音/取消静音 Mumble 的麦克风和音频输出：

`mumble rpc {{deaf|undeaf}}`