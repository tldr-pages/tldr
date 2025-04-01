# taskset

> 获取或设置进程的 CPU 亲和性，或者以指定的 CPU 亲和性启动新进程。
> 更多信息：<https://manned.org/taskset>.

- 通过进程 ID 获取运行中进程的 CPU 亲和性：

`taskset {{[-p|--pid]}} {{[-c|--cpu-list]}} {{pid}}`

- 通过进程 ID 设置运行中进程的 CPU 亲和性：

`taskset {{[-p|--pid]}} {{[-c|--cpu-list]}} {{cpu_id}} {{pid}}`

- 以单个 CPU 的亲和性启动新进程：

`taskset {{[-c|--cpu-list]}} {{cpu_id}} {{command}}`

- 以多个非连续 CPU 的亲和性启动新进程：

`taskset {{[-c|--cpu-list]}} {{cpu_id_1}},{{cpu_id_2}},{{cpu_id_3}}`

- 以 CPU 1 到 4 的亲和性启动新进程：

`taskset {{[-c|--cpu-list]}} {{cpu_id_1}}-{{cpu_id_4}}`
