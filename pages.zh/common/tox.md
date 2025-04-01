# tox

> 自动化跨多个 Python 版本的测试。
> 使用 tox.ini 配置环境和测试命令。
> 更多信息：<https://github.com/tox-dev/tox>.

- 在所有测试环境中运行测试：

`tox`

- 创建一个 `tox.ini` 配置：

`tox-quickstart`

- 列出所有可用的环境：

`tox --listenvs-all`

- 在特定环境（例如 Python 3.6）中运行测试：

`tox -e {{py36}}`

- 强制重新创建虚拟环境：

`tox --recreate -e {{py27}}`