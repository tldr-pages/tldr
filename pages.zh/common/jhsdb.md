# jhsdb

> 附加到一个 Java 进程或启动后期调试器以分析崩溃的 Java 虚拟机的核心转储。
> 更多信息：<https://manned.org/jhsdb>。

- 打印 Java 进程的堆栈和锁信息：

`jhsdb jstack --pid {{pid}}`

- 以交互调试模式打开核心转储：

`jhsdb clhsdb --core {{path/to/core_dump}} --exe {{path/to/jdk/bin/java}}`

- 启动远程调试服务器：

`jhsdb debugd --pid {{pid}} --serverid {{optional_unique_id}}`

- 以交互调试模式连接到进程：

`jhsdb clhsdb --pid {{pid}}`