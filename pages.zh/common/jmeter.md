# jmeter

> 开源的 Java 应用程序，旨在对功能行为进行负载测试并衡量性能。
> 更多信息：<https://jmeter.apache.org>.

- 在非 GUI 模式下运行指定的测试计划：

`jmeter --nongui --testfile {{路径/到/文件.jmx}}`

- 在非 GUI 模式下使用指定的日志文件运行测试计划：

`jmeter --nogui --testfile {{路径/到/文件.jmx}} --logfile {{路径/到/日志文件.jtl}}`

- 在非 GUI 模式下使用指定代理运行测试计划：

`jmeter --nongui --testfile {{路径/到/文件.jmx}} --proxyHost {{127.0.0.1}} --proxyPort {{8888}}`

- 在非 GUI 模式下使用指定的 JMeter 属性运行测试计划：

`jmeter --jmeterproperty {{键}}='{{值}}' --nongui --testfile {{路径/到/文件.jmx}}`
