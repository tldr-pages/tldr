# waypipe

> 在 Wayland 合成器下远程运行图形应用程序。
> 更多信息：<https://gitlab.freedesktop.org/mstoeckl/waypipe>.

- 远程运行图形程序并本地显示：

`waypipe ssh {{user}}@{{server}} {{program}}`

- 打开 SSH 隧道以远程运行任何程序并本地显示：

`waypipe ssh {{user}}@{{server}}`

- 跳过 Vulkan 支持测试：

`waypipe --test-skip-vulkan ssh {{user}}@{{server}} {{program}}`

- 显示帮助：

`waypipe {{[-h|--help]}}`
