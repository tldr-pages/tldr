# pipx

> 在隔离的环境中安装和运行 Python 应用程序。
> 更多信息：<https://github.com/pypa/pipx>。

- 在临时虚拟环境中运行应用程序：

`pipx run {{pycowsay}} {{moo}}`

- 在虚拟环境中安装包，并将入口点添加到路径中：

`pipx install {{package}}`

- 列出已安装的包：

`pipx list`

- 在临时虚拟环境中运行应用程序，应用程序名称与可执行文件名称不同：

`pipx run --spec {{httpx-cli}} {{httpx}} {{http://www.github.com}}`

- 将依赖项注入到现有的虚拟环境中：

`pipx inject {{package}} {{dependency1 dependency2 ...}}`

- 使用 pip 参数在虚拟环境中安装包：

`pipx install --pip-args='{{pip-args}}' {{package}}`

- 升级/重新安装/卸载所有已安装的包：

`pipx {{upgrade-all|uninstall-all|reinstall-all}}`