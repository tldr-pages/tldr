# uv venv

> 创建一个用于安装软件包的隔离 Python 环境。
> 更多信息：<https://docs.astral.sh/uv/reference/cli/#uv-venv>.

- 在默认位置创建虚拟环境（`.venv`）：

`uv venv`

- 在特定路径下创建一个虚拟环境：

`uv venv {{路径/到/虚拟环境}}`

- 使用特定的 Python 版本创建：

`uv venv --python {{3.12}}`

- 使用自定义提示词前缀进行创建：

`uv venv --prompt {{我的_项目}}`

- 创建并允许覆盖现有环境：

`uv venv --allow-existing {{虚拟环境_名称}}`
