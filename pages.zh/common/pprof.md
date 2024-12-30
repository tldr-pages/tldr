# pprof

> 这是一个用于可视化和分析性能数据的命令行工具。
> 更多信息请访问：<https://github.com/google/pprof>。

- 从特定的性能文件生成文本报告，针对 fibbo 二进制文件：

`pprof -top {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- 生成图形并在网页浏览器中打开：

`pprof -svg {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- 以交互模式运行 pprof，以便手动对文件启动 `pprof`：

`pprof {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- 运行一个网络服务器，在 `pprof` 之上提供一个网页界面：

`pprof -http={{localhost:8080}} {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- 从 HTTP 服务器获取性能数据并生成报告：

`pprof {{http://localhost:8080/debug/pprof}}`