# gum

> 让你的 shell 脚本更加优雅。
> 更多信息：<https://github.com/charmbracelet/gum>.

- 交互式地选择一个特定的选项并打印到 `stdout`：

`gum choose "{{option_1}}" "{{option_2}}" "{{option_3}}"`

- 打开一个交互式提示，让用户输入带有特定占位符的字符串：

`gum input --placeholder "{{value}}"`

- 打开一个交互式确认提示，并根据选择退出返回 `<0>` 或 `<1>`：

`gum confirm "{{Continue?}}" --default=false --affirmative "{{Yes}}" --negative "{{No}}" {{&& echo "Yes selected" || echo "No selected"}}`

- 在命令执行时显示带有文本的加载动画：

`gum spin --spinner {{dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger}} --title "{{loading...}}" -- {{command}}`

- 格式化文本以包含表情符号：

`gum format -t {{emoji}} "{{:smile: :heart: hello}}"`

- 交互式地输入多行文本（使用 `<Ctrl d>` 保存）并写入 `data.txt`：

`gum write > {{data.txt}}`
