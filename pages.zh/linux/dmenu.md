# dmenu

> 动态菜单。
> 从文本输入创建菜单，每个项目占一行。
> 更多信息：<https://manned.org/dmenu>。

- 显示 `ls` 命令输出的菜单：

`{{ls}} | dmenu`

- 显示带有自定义项目的菜单，项目之间用换行符（`\n`）分隔：

`echo -e "{{red}}\n{{green}}\n{{blue}}" | dmenu`

- 让用户在多个项目中选择，并将所选项目保存到文件中：

`echo -e "{{red}}\n{{green}}\n{{blue}}" | dmenu > {{color.txt}}`

- 在特定的显示器上启动 dmenu：

`ls | dmenu -m {{1}}`

- 在屏幕底部显示 dmenu：

`ls | dmenu -b`