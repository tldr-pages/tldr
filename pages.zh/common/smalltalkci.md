# smalltalkci

> 用于使用 GitHub Actions、Travis CI、AppVeyor、GitLab CI 等测试 Smalltalk 项目的框架。
> 更多信息：<https://github.com/hpi-swa/smalltalkCI>。

- 运行配置文件的测试：

`smalltalkci {{path/to/.smalltalk.ston}}`

- 运行当前目录中 `.smalltalk.ston` 配置的测试：

`smalltalkci`

- 在带有窗口的模式下调试测试（显示虚拟机窗口）：

`smalltalkci --headful`

- 下载并准备一个众所周知的 Smalltalk 镜像以进行测试：

`smalltalkci --smalltalk {{Squeak64-Trunk}}`

- 指定自定义的 Smalltalk 镜像和虚拟机：

`smalltalkci --image {{path/to/Smalltalk.image}} --vm {{path/to/vm}}`

- 清理缓存并删除构建：

`smalltalkci --clean`