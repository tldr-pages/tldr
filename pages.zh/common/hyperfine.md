# hyperfine

> 一个命令行基准测试工具。
> 更多信息：<https://github.com/sharkdp/hyperfine/>.

- 运行一个基本的基准测试，至少执行 10 次：

`hyperfine '{{make}}'`

- 运行一个比较基准测试：

`hyperfine '{{make target1}}' '{{make target2}}'`

- 更改变基准测试的最小运行次数：

`hyperfine --min-runs {{7}} '{{make}}'`

- 带有预热运行的基准测试：

`hyperfine --warmup {{5}} '{{make}}'`

- 在每次基准测试运行前运行一个命令（例如清理缓存等）：

`hyperfine --prepare '{{make clean}}' '{{make}}'`

- 在每次运行中改变单个参数的基准测试：

`hyperfine --prepare '{{make clean}}' --parameter-scan {{num_threads}} {{1}} {{10}} '{{make -j {num_threads}}}'`