# jhat

> Java 堆分析工具。
> 更多信息：<https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html>。

- 分析堆转储（来自 `jmap`），通过 HTTP 在 7000 端口查看：

`jhat {{dump_file.bin}}`

- 分析堆转储，指定 HTTP 服务器的备用端口：

`jhat -p {{port}} {{dump_file.bin}}`

- 分析转储，允许 `jhat` 使用最多 8 GB 的 RAM（建议为转储大小的 2-4 倍）：

`jhat -J-mx8G {{dump_file.bin}}`