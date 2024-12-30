# virtualenvwrapper

> 一组用于 Python 的 `virtualenv` 工具的简单包装命令。
> 更多信息：<https://virtualenvwrapper.readthedocs.org>。

- 在 `$WORKON_HOME` 中创建一个新的 Python `virtualenv`：

`mkvirtualenv {{virtualenv_name}}`

- 为特定的 Python 版本创建一个 `virtualenv`：

`mkvirtualenv --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- 激活或使用不同的 `virtualenv`：

`workon {{virtualenv_name}}`

- 停止 `virtualenv`：

`deactivate`

- 列出所有虚拟环境：

`lsvirtualenv`

- 删除一个 `virtualenv`：

`rmvirtualenv {{virtualenv_name}}`

- 获取所有 virtualenvwrapper 命令的摘要：

`virtualenvwrapper`