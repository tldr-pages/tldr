# nice

> 使用自定义调度优先级（亲和度）执行程序。
> 亲和度值范围从 -20（最高优先级）到 19（最低优先级）。
> 更多信息：<https://www.gnu.org/software/coreutils/nice>。

- 启动具有更改优先级的程序：

`nice -{{niceness_value}} {{command}}`

- 使用显式选项定义优先级：

`nice {{-n|--adjustment}} {{niceness_value}} {{command}}`