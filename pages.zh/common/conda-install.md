# conda 安装

> 将软件包安装到现有的 conda 环境中。
> 更多信息：<https://docs.conda.io/projects/conda/en/latest/commands/install.html>。

- 在当前活动的 conda 环境中安装一个或多个软件包：

`conda install {{package1 package2 ...}}`

- 使用 conda-forge 渠道在当前活动的 conda 环境中安装单个软件包：

`conda install -c conda-forge {{package}}`

- 使用 conda-forge 渠道在当前活动的 conda 环境中安装单个软件包，并忽略其他渠道：

`conda install -c conda-forge --override-channels {{package}}`

- 安装特定版本的软件包：

`conda install {{package}}={{version}}`

- 将软件包安装到特定环境中：

`conda install --name {{environment}} {{package}}`

- 更新当前环境中的软件包：

`conda install --upgrade {{package}}`

- 安装软件包并在不提示的情况下同意交易：

`conda install --yes {{package}}`