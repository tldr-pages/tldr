# hyperfine

> 一个基准测试工具。
> 更多信息：<https://manned.org/hyperfine>。

- 运行基础基准测试，至少执行 10 轮：

`hyperfine '{{make}}'`

- 运行对比基准测试：

`hyperfine '{{make target1}}' '{{make target2}}'`

- 修改基准测试的最少轮数：

`hyperfine {{[-m|--min-runs]}} {{7}} '{{make}}'`

- 带预热运行基准测试：

`hyperfine {{[-w|--warmup]}} {{5}} '{{make}}'`

- 每轮基准测试前先运行一条命令（例如清空缓存）：

`hyperfine {{[-p|--prepare]}} '{{make clean}}' '{{make}}'`

- 运行每轮只有一个参数变化的基准测试：

`hyperfine {{[-p|--prepare]}} '{{make clean}}' {{[-P|--parameter-scan]}} {{num_threads}} {{1}} {{10}} '{{make --jobs {num_threads}}}'`
