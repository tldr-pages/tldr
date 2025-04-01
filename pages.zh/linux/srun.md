# srun

> 创建一个交互式的 Slurm 作业或连接到现有作业。
> 更多信息：<https://slurm.schedmd.com/srun.html>.

- 提交一个基本的交互式作业：

`srun --pty /bin/bash`

- 提交具有不同属性的交互式作业：

`srun --ntasks-per-node={{num_cores}} --mem-per-cpu={{memory_MB}} --pty /bin/bash`

- 连接到运行作业的工作节点：

`srun --jobid={{job_id}} --pty /bin/bash`
