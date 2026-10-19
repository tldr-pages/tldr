# hyperfine

> 一个基准测试工具。
> 更多信息：<https://manned.org/hyperfine>.

- 运行一个基本基准测试，至少执行 10 次：

`hyperfine '{{make}}'`

- 运行一个对比基准测试：

`hyperfine '{{make target1}}' '{{make target2}}'`

- 修改基准测试的最少运行次数：

`hyperfine {{[-m|--min-runs]}} {{7}} '{{make}}'`

- 带预热执行基准测试：

`hyperfine {{[-w|--warmup]}} {{5}} '{{make}}'`

- 在每次基准测试运行前执行一个命令（用于清除缓存等）：

`hyperfine {{[-p|--prepare]}} '{{make clean}}' '{{make}}'`

- 运行一个每次运行都改变单个参数的基准测试：

`hyperfine {{[-p|--prepare]}} '{{make clean}}' {{[-P|--parameter-scan]}} {{num_threads}} {{1}} {{10}} '{{make --jobs {num_threads}}}'
