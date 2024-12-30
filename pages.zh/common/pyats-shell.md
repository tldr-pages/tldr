# pyats shell

> 启动一个预加载的 pyATS 交互式 Python Shell，以节省原型设计的时间。
> 更多信息：<https://pubhub.devnetcloud.com/media/genie-docs/docs/cli/genie_shell.html>。

- 使用定义的测试床文件打开 pyATS shell：

`pyats shell --testbed-file {{path/to/testbed.yaml}}`

- 使用定义的 Pickle 文件打开 pyATS shell：

`pyats shell --pickle-file {{path/to/pickle.file}}`

- 在不启用 IPython 的情况下打开 pyATS：

`pyats shell --no-ipython`