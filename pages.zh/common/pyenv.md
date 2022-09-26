# pyenv

> 在多个 Python 版本之间轻松切换。
> 更多信息：<https://github.com/pyenv/pyenv>.

- 列出所有可用的命令：

`pyenv commands`

- 列出 `${PYENV_ROOT}/versions` 目录下的所有 Python 版本：

`pyenv versions`

- 在 `${PYENV_ROOT}/versions` 目录下安装一个 Python 版本：

`pyenv install {{2.7.10}}`

- 在 `${PYENV_ROOT}/versions` 目录下卸载一个 Python 版本：

`pyenv uninstall {{2.7.10}}`

- 设置在当前机器中全局使用的 Python 版本：

`pyenv global {{2.7.10}}`

- 设置在当前目录及其下所有目录中使用的 Python 版本：

`pyenv local {{2.7.10}}`
