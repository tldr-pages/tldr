# until

> 简单的 shell 循环，直到接收到零作为返回值才会停止。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-until>.

- 直到命令成功才退出：

`until {{command}}; do :; done`

- 等待一个 systemd 服务变得活跃：

`until systemctl is-active {{[-q|--quiet]}} {{nginx}}; do {{echo "等待中..."}}; sleep 1; done; {{echo "启动成功！"}}`