# taskset

> 获取或设置进程的 CPU 亲和性，或以定义的 CPU 亲和性启动一个新进程。
> 更多信息：<https://manned.org/taskset>。

- 通过 PID 获取正在运行的进程的 CPU 亲和性：

`taskset --pid --cpu-list {{pid}}`

- 通过 PID 设置正在运行的进程的 CPU 亲和性：

`taskset --pid --cpu-list {{cpu_id}} {{pid}}`

- 启动一个仅与单个 CPU 亲和的新进程：

`taskset --cpu-list {{cpu_id}} {{command}}`

- 启动一个与多个非连续 CPU 亲和的新进程：

`taskset --cpu-list {{cpu_id_1}},{{cpu_id_2}},{{cpu_id_3}}`

- 启动一个与 CPU 1 到 4 亲和的新进程：

`taskset --cpu-list {{cpu_id_1}}-{{cpu_id_4}}`