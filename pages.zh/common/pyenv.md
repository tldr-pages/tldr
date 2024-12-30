# pyenv

> 轻松切换多个Python版本。
> 另请参见： `asdf`。
> 更多信息： <https://github.com/pyenv/pyenv>。

- 列出所有可用命令：

`pyenv commands`

- 列出`${PYENV_ROOT}/versions`目录下的所有Python版本：

`pyenv versions`

- 列出可以从上游安装的所有Python版本：

`pyenv install --list`

- 在`${PYENV_ROOT}/versions`目录下安装一个Python版本：

`pyenv install {{2.7.10}}`

- 卸载`${PYENV_ROOT}/versions`目录下的一个Python版本：

`pyenv uninstall {{2.7.10}}`

- 设置当前机器上全局使用的Python版本：

`pyenv global {{2.7.10}}`

- 设置当前目录及其所有子目录中使用的Python版本：

`pyenv local {{2.7.10}}`