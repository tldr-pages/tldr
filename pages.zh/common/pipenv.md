# pipenv

> 简单统一的Python开发工作流程。
> 管理项目的包和虚拟环境。
> 更多信息：<https://pypi.org/project/pipenv>。

- 创建一个新项目：

`pipenv`

- 使用Python 3创建一个新项目：

`pipenv --three`

- 安装一个包：

`pipenv install {{package}}`

- 安装项目的所有依赖项：

`pipenv install`

- 安装项目的所有依赖项（包括开发包）：

`pipenv install --dev`

- 卸载一个包：

`pipenv uninstall {{package}}`

- 在创建的虚拟环境中启动一个shell：

`pipenv shell`

- 为项目生成一个 `requirements.txt`（依赖项列表）：

`pipenv lock --requirements`