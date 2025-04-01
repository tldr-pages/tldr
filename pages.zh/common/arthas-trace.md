# arthas-trace

> 方法内部调用路径，并输出方法路径上的每个节点上耗时。
> 另见 `arthas`, `arthas-watch`.
> 更多信息：<https://arthas.aliyun.com/en/doc/trace.html>.

- 追踪方法调用链：

`trace {{class-pattern}} {{method-pattern}}`

- 追踪方法调用链，仅显示大于 10 毫秒的调用：

`trace {{class-pattern}} {{method-pattern}} '#cost > {{10}}'`

- 追踪多个类和方法的调用：

`trace -E {{class-pattern1|class-patter2}} {{method-pattern1|method-pattern2|method-pattern3}}`

- 仅显示大于 10 毫秒的调用链，观测 10 次：

`trace {{class-pattern}} {{method-pattern}} '#cost > {{10}}' -n 5`
