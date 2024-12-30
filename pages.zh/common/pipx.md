# pipx

> 在隔离环境中安装和运行Python应用程序。
> 更多信息：<https://github.com/pypa/pipx>。

- 在临时虚拟环境中运行应用程序：

`pipx run {{pycowsay}} {{moo}}`

- 在虚拟环境中安装包并将入口点添加到路径中：

`pipx install {{package}}`

- 列出已安装的包：

`pipx list`

- 在临时虚拟环境中运行应用程序，执行文件名与包名不同：

`pipx run --spec {{httpx-cli}} {{httpx}} {{http://www.github.com}}`

- 将依赖项注入到现有虚拟环境中：

`pipx inject {{package}} {{dependency1 dependency2 ...}}`

- 在虚拟环境中使用pip参数安装包：

`pipx install --pip-args='{{pip-args}}' {{package}}`

- 升级/重新安装/卸载所有已安装的包：

`pipx {{upgrade-all|uninstall-all|reinstall-all}}`