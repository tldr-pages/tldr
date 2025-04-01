# conda install

> 在现有的 conda 环境中安装包。
> 更多信息：<https://docs.conda.io/projects/conda/en/latest/commands/install.html>。

- 在当前激活的 conda 环境中安装一个或多个包：

`conda install {{package1 package2 ...}}`

- 使用 conda-forge 渠道在当前激活的 conda 环境中安装单个包：

`conda install -c conda-forge {{package}}`

- 使用 conda-forge 渠道并在忽略其他渠道的情况下，在当前激活的 conda 环境中安装单个包：

`conda install -c conda-forge --override-channels {{package}}`

- 安装特定版本的包：

`conda install {{package}}={{version}}`

- 在特定环境中安装包：

`conda install --name {{environment}} {{package}}`

- 更新当前环境中的包：

`conda install --upgrade {{package}}`

- 安装包并同意交易而不提示：

`conda install --yes {{package}}`
