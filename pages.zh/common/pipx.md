# pipx

> 在隔离环境中安装并运行 Python 应用程序。
> 更多信息：<https://github.com/pypa/pipx>.

- 在临时虚拟环境中运行应用程序：

`pipx run {{pycowsay}} {{moo}}`

- 在虚拟环境中安装包并将入口点添加到路径：

`pipx install {{package}}`

- 列出已安装包：

`pipx list`

- 在临时虚拟环境中运行应用程序（当包名与可执行文件不同时）：

`pipx run --spec {{httpx-cli}} {{httpx}} {{http://www.github.com}}`

- 向现有虚拟环境注入依赖项：

`pipx inject {{package}} {{dependency1 dependency2 ...}}`

- 使用 pip 参数在虚拟环境中安装包：

`pipx install --pip-args='{{pip-args}}' {{package}}`

- 升级/卸载/重装所有已安装包：

`pipx {{upgrade-all|uninstall-all|reinstall-all}}`
