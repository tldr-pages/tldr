# conda create

> 创建新的 conda 环境。
> 更多信息：<https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- 创建一个名为 `py39` 的新环境，并在其中安装 Python 3.9 和 NumPy 1.11 或更高版本：

`conda create --yes --name {{py39}} python={{3.9}} "{{numpy>=1.11}}"`

- 创建一个环境的精确副本：

`conda create --clone {{py39}} --name {{py39-copy}}`

- 创建一个具有指定名称的新环境并安装指定的软件包：

`conda create --name {{env_name}} {{package}}`