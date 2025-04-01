# kdialog

> 在 shell 脚本中显示 KDE 对话框。
> 更多信息：<https://develop.kde.org/docs/administration/kdialog/>.

- 打开一个显示特定消息的对话框：

`kdialog --msgbox "{{message}}" "{{optional_detailed_message}}"`

- 打开一个带有“是”和“否”按钮的提问对话框，分别返回 `0` 和 `1`：

`kdialog --yesno "{{message}}"`

- 打开一个带有“是”、“否”和“取消”按钮的警告对话框，分别返回 `0`、`1` 或 `2`：

`kdialog --warningyesnocancel "{{message}}"`

- 打开一个输入对话框，并在按下“确定”时将输入打印到 `stdout`：

`kdialog --inputbox "{{message}}" "{{optional_default_text}}"`

- 打开一个提示输入特定密码的对话框，并将其打印到 `stdout`：

`kdialog --password "{{message}}"`

- 打开一个包含特定下拉菜单的对话框，并将选中的项目打印到 `stdout`：

`kdialog --combobx "{{message}}" "{{item1}}" "{{item2}}" "{{...}}"`

- 打开一个文件选择对话框，并将选中的文件路径打印到 `stdout`：

`kdialog --getopenfilename`

- 打开一个进度条对话框，并将用于通信的 D-Bus 引用打印到 `stdout`：

`kdialog --progressbar "{{message}}"`
