# virtualenvwrapper

> Python 的 `virtualenv` 工具的简单命令包装器组。
> 更多信息：<https://virtualenvwrapper.readthedocs.org>。

- 在 `$WORKON_HOME` 中创建一个新的 Python `virtualenv`：

`mkvirtualenv {{virtualenv_name}}`

- 为特定 Python 版本创建一个 `virtualenv`：

`mkvirtualenv --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- 激活或切换到不同的 `virtualenv`：

`workon {{virtualenv_name}}`

- 退出当前 `virtualenv`：

`deactivate`

- 列出所有虚拟环境：

`lsvirtualenv`

- 删除一个 `virtualenv`：

`rmvirtualenv {{virtualenv_name}}`

- 获取所有 virtualenvwrapper 命令的概要：

`virtualenvwrapper`