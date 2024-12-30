# jupyter

> 用于创建和分享包含代码、可视化和笔记的文档的 web 应用程序。
> 主要用于数据分析、科学计算和机器学习。
> 更多信息：<https://jupyter.org>。

- 在当前目录启动 Jupyter notebook 服务器：

`jupyter notebook`

- 打开特定的 Jupyter notebook：

`jupyter notebook {{example.ipynb}}`

- 将特定的 Jupyter notebook 导出为另一种格式：

`jupyter nbconvert --to {{html|markdown|pdf|script}} {{example.ipynb}}`

- 在特定端口启动服务器：

`jupyter notebook --port={{port}}`

- 列出当前正在运行的 notebook 服务器：

`jupyter notebook list`

- 停止当前正在运行的服务器：

`jupyter notebook stop`

- 在当前目录启动 JupyterLab（如果已安装）：

`jupyter lab`