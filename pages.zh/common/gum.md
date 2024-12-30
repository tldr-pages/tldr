# gum

> 制作华丽的shell脚本。
> 更多信息：<https://github.com/charmbracelet/gum>。

- 以交互方式选择特定选项并打印到`stdout`：

`gum choose "{{option_1}}" "{{option_2}}" "{{option_3}}"`

- 为用户打开一个交互式提示，输入带有特定占位符的字符串：

`gum input --placeholder "{{value}}"`

- 打开一个交互式确认提示，并以`0`或`1`退出：

`gum confirm "{{继续？}}" --default=false --affirmative "{{是}}" --negative "{{否}}" {{&& echo "选择了是" || echo "选择了否"}}`

- 在命令执行时显示旋转器，并旁边附上文本：

`gum spin --spinner {{dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger}} --title "{{加载中...}}" -- {{command}}`

- 格式化文本以包含表情符号：

`gum format -t {{emoji}} "{{:smile: :heart: 你好}}"`

- 交互式提示输入多行文本（CTRL + D 保存），并写入`data.txt`：

`gum write > {{data.txt}}`