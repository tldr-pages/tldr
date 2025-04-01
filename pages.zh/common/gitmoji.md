# gitmoji

> 交互式地在提交中插入表情符号。
> 更多信息：<https://github.com/carloscuesta/gitmoji-cli>。

- 启动提交向导：

`gitmoji --commit`

- 初始化 Git 钩子（这样每次运行 `git commit` 时，都会运行 `gitmoji`）：

`gitmoji --init`

- 移除 Git 钩子：

`gitmoji --remove`

- 列出所有可用的表情符号及其描述：

`gitmoji --list`

- 搜索表情符号列表中的关键词：

`gitmoji --search {{keyword1}} {{keyword2}}`

- 从主仓库更新缓存的表情符号列表：

`gitmoji --update`

- 配置全局偏好设置：

`gitmoji --config`