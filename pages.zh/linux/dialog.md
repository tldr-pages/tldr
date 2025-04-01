# dialog

> 在终端上显示对话框。
> 更多信息：<https://manned.org/dialog>.

- 显示消息：

`dialog --msgbox "{{消息}}" {{高度}} {{宽度}}`

- 提示用户输入文本：

`dialog --inputbox "{{输入文本:}}" {{8}} {{40}} 2>{{output.txt}}`

- 提示用户进行是/否选择：

`dialog --yesno "{{继续吗?}}" {{7}} {{40}}`

- 显示帮助：

`dialog`
