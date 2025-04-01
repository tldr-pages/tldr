# pipenv

> 简单统一的 Python 开发工作流。
> 管理项目中的包和虚拟环境。
> 更多信息：<https://pypi.org/project/pipenv>.

- 创建新项目：

`pipenv`

- 使用 Python 3 创建新项目：

`pipenv --three`

- 安装包：

`pipenv install {{package}}`

- 安装项目的依赖项：

`pipenv install`

- 安装项目的依赖项（包括开发包）：

`pipenv install --dev`

- 卸载包：

`pipenv uninstall {{package}}`

- 在创建的虚拟环境中启动 shell：

`pipenv shell`

- 为项目生成 `requirements.txt`（依赖列表）：

`pipenv lock --requirements`
