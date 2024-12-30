# jmeter

> 一个开源的Java应用程序，旨在进行负载测试功能行为和性能测量。
> 更多信息：<https://jmeter.apache.org>。

- 在无GUI模式下运行特定的测试计划：

`jmeter --nongui --testfile {{path/to/file.jmx}}`

- 使用特定日志文件在无GUI模式下运行测试计划：

`jmeter --nogui --testfile {{path/to/file.jmx}} --logfile {{path/to/logfile.jtl}}`

- 使用特定代理在无GUI模式下运行测试计划：

`jmeter --nongui --testfile {{path/to/file.jmx}} --proxyHost {{127.0.0.1}} --proxyPort {{8888}}`

- 使用特定JMeter属性在无GUI模式下运行测试计划：

`jmeter --jmeterproperty {{key}}='{{value}}' --nongui --testfile {{path/to/file.jmx}}`