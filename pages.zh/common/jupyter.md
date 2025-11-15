# jupyter

> 用于创建和共享包含代码、可视化和笔记的文档的 Web 应用程序。
> 主要用于数据分析、科学计算和机器学习。
> 更多信息：<https://docs.jupyter.org/en/latest/>.

- 在当前目录下启动一个 Jupyter notebook 服务器：

`jupyter notebook`

- 打开一个特定的 Jupyter notebook：

`jupyter notebook {{示例.ipynb}}`

- 将特定 Jupyter notebook 导出为其他格式：

`jupyter nbconvert --to {{html|markdown|pdf|script}} {{示例.ipynb}}`

- 在指定端口启动服务器：

`jupyter notebook --port {{端口}}`

- 列出当前正在运行的 notebook 服务器：

`jupyter notebook list`

- 停止当前正在运行的服务器：

`jupyter notebook stop`

- 启动 JupyterLab（如果已安装）于当前目录：

`jupyter lab`
