# qsub

> 向队列管理系统 TORQUE 提交脚本。
> 更多信息：<https://manned.org/qsub.1>.

- 使用默认设置提交脚本（取决于 TORQUE 设置）：

`qsub {{script.sh}}`

- 提交一个指定运行时间为 1 小时 2 分钟 3 秒的脚本：

`qsub -l walltime={{1}}:{{2}}:{{3}} {{script.sh}}`

- 提交一个将在 2 个节点上执行，每个节点使用 4 个核心的脚本：

`qsub -l nodes={{2}}:ppn={{4}} {{script.sh}}`

- 将脚本提交到特定的队列。请注意，不同的队列可能有不同的最大和最小运行时间限制：

`qsub -q {{queue_name}} {{script.sh}}`
