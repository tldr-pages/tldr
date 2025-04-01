# rc

> 一个现代的简化端口监听器和反向 shell。
> 类似于 `nc`。
> 更多信息：<https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- 在特定端口上开始监听：

`rc -lp {{port}}`

- 启动反向 shell：

`rc {{host}} {{port}} -r {{shell}}`
