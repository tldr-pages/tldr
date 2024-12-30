# qsub

> 将脚本提交到队列管理系统 TORQUE。
> 更多信息：<https://manned.org/qsub.1>。

- 使用默认设置提交脚本（依赖于 TORQUE 设置）：

`qsub {{script.sh}}`

- 提交一个指定墙钟运行时间限制为 1 小时、2 分钟和 3 秒的脚本：

`qsub -l walltime={{1}}:{{2}}:{{3}} {{script.sh}}`

- 提交一个在 2 个节点上使用每个节点 4 个核心执行的脚本：

`qsub -l nodes={{2}}:ppn={{4}} {{script.sh}}`

- 将脚本提交到特定队列。请注意，不同的队列可能有不同的最大和最小运行时间限制：

`qsub -q {{queue_name}} {{script.sh}}`