# hyperfine

> 一款命令行基准测试工具。
> 更多信息：<https://github.com/sharkdp/hyperfine/>.

- 运行基本基准测试，至少执行 10 次：

`hyperfine '{{make}}'`

- 运行比较基准测试：

`hyperfine '{{make target1}}' '{{make target2}}'`

- 更改最小基准测试运行次数：

`hyperfine --min-runs {{7}} '{{make}}'`

- 执行包含预热的基准测试：

`hyperfine --warmup {{5}} '{{make}}'`

- 在每次基准测试运行之前运行一个命令（用于清除缓存等）：

`hyperfine --prepare '{{make clean}}' '{{make}}'`

- 运行一个基准测试，其中每次运行时单个参数发生变化：

`hyperfine --prepare '{{make clean}}' --parameter-scan {{num_threads}} {{1}} {{10}} '{{make -j {num_threads}}}'`