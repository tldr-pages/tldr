# conda list

> 列出一个 conda 环境中已安装的包。
> 更多信息：<https://docs.conda.io/projects/conda/en/stable/commands/list.html>.

- 列出当前环境中的所有包：

`conda list`

- 列出指定环境的包：

`conda list {{[-n|--name]}} {{环境名称}}`

- 列出特定路径下安装的包：

`conda list {{[-p|--prefix]}} {{路径/到/环境}}`

- 用 `正则表达式` 过滤安装的包：

`conda list {{正则表达式}}`

- 保存包列表，以供以后使用：

`conda list {{[-e|--export]}} > {{路径/到/包列表.txt}}`
