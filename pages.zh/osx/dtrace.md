# dtrace

> 一个简单的接口，用于调用 D 语言编译器，检索缓冲的跟踪数据，并从 DTrace 内核设施打印跟踪数据。
> DTrace 设施的通用前端，需要 root 权限。
> 更多信息：<https://keith.github.io/xcode-man-pages/dtrace.1.html>.

- 为特定架构设置目标数据模型：

`dtrace -arch {{arch_name}}`

- 声明 [a]nonymous 跟踪状态并显示跟踪数据：

`dtrace -a`

- 设置主要跟踪缓冲区大小。支持的单位有 `k`、`m`、`g` 或 `t`：

`dtrace -b {{2g}}`

- 编译指定的 D 程序 [s]ource 文件：

`dtrace -s {{D_script}}`

- 运行指定的 [c]ommand 并在其完成后退出：

`dtrace -c {{command}}`

- 指定要跟踪或列出（-l 选项）的 [f]unction 名称。对应的参数可以包括任何形式的探针描述，如 `provider:module:function`、`module:function` 或 `function`：

`dtrace -f {{function}}`

- 获取指定的 [p]rocess ID，缓存其符号表，并在其完成后退出：

`dtrace -p {{pid}}`

- 结合不同选项以在进程中跟踪函数：

`dtrace -a -b {{buffer_size}} -f {{function}} -p {{pid}}`