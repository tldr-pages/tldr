# 直到

> 简单的 shell 循环，直到接收到零作为返回值为止。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-until>。

- 执行命令直到成功为止：

`until {{command}}; do :; done`

- 等待 systemd 服务变为活动状态：

`until systemctl is-active --quiet {{nginx}}; do {{echo "等待..."}}; sleep 1; done; {{echo "启动完成！"}}`