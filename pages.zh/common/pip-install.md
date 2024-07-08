# pip install

> 用于安装 Python 包。
> 更多信息：<https://pip.pypa.io/>.

- 安装指定包：

`pip install {{包名}}`

- 安装指定版本的包：

`pip install "{{包名}}=={{版本号}}"`

- 安装满足最低版本要求的包：

`pip install "{{包名}}>={{版本号}}"`

- 通过指定的依赖文件安装（通常文件名是 requirements.txt）:

`pip install -r requirements.txt`

- 通过 wheels 文件（扩展名 *.whl）安装：

`pip install {{包名-1.0-py2.py3-none-any.whl}}`

- 通过源码存档文件安装（如 *.tar.gz）：

`pip install {{源存档文件路径}}`

- 通过版本控制软件提供的项目 URL 安装：

`pip install {{项目仓库URL}}`

- 在本地的项目路径下安装（通常是读取 pyproject.toml 或 setup.py 文件）：

`pip install .`
