# arthas-trace

> Trace method invoke chain, and output the time cost for each node in the path.
> See also: `arthas`, `arthas-watch`.
> More information: <https://arthas.aliyun.com/en/doc/trace.html>.

- Trace method invoke chain:

`trace {{class_pattern}} {{method_pattern}}`

- Trace method invoke chains and only display invoke information longer than 10 ms:

`trace {{class_pattern}} {{method_pattern}} '#cost > {{10}}'`

- Trace the invoke chain of multiple classes or multiple methods:

`trace -E {{class_pattern1}}|{{class_pattern2}} {{method_pattern1}}|{{method_pattern2}}|{{method_pattern3}}`

- Track method invoke chains, only display invoke information that exceeds 10 ms, and exit after 5 times:

`trace {{class_pattern}} {{method_pattern}} '#cost > {{10}}' -n 5`
