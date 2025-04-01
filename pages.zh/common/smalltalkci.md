# smalltalkci

> 用于使用 GitHub Actions、Travis CI、AppVeyor、GitLab CI 等工具测试 Smalltalk 项目的框架。
> 更多信息：<https://github.com/hpi-swa/smalltalkCI>.

- 为配置文件运行测试：

`smalltalkci {{path/to/.smalltalk.ston}}`

- 为当前目录中的 `.smalltalk.ston` 配置文件运行测试：

`smalltalkci`

- 以头部模式调试测试（显示 VM 窗口）：

`smalltalkci --headful`

- 下载并准备一个知名的小型镜像用于测试：

`smalltalkci --smalltalk {{Squeak64-Trunk}}`

- 指定自定义的 Smalltalk 镜像和 VM：

`smalltalkci --image {{path/to/Smalltalk.image}} --vm {{path/to/vm}}`

- 清理缓存并删除构建：

`smalltalkci --clean`
