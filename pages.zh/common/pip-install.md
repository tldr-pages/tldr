# pip install

> 用于安装 Python 包。
> 更多信息：<https://pip.pypa.io/en/stable/cli/pip_install/>.

- 安装包：

`pip install {{包名}}`

- 安装指定版本的包：

`pip install {{包名}}=={{版本号}}`

- 通过指定的依赖文件安装（通常文件名是 requirements.txt）：

`pip install {{[-r|--requirement]}} {{requirements.txt}}`

- 通过 URL 或源码存档文件安装（如 *.tar.gz 或 *.whl）：

`pip install {{[-f|--find-links]}} {{url|存档文件}}`

- 在本地的项目路径下以开发模式（editable）安装（通常是读取 pyproject.toml 或 setup.py 文件）：

`pip install {{[-e|--editable]}} .`
