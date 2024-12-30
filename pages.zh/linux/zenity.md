# zenity

> 从命令行/脚本显示对话框。
> 返回用户输入的值或在出错时返回1。
> 更多信息：<https://manned.org/zenity>。

- 显示默认的询问对话框：

`zenity --question`

- 显示一个信息对话框，显示文本“Hello!”：

`zenity --info --text="{{Hello!}}"`

- 显示一个姓名/密码表单，并输出用“;”分隔的数据：

`zenity --forms --add-entry="{{Name}}" --add-password="{{Password}}" --separator="{{;}}"`

- 显示一个文件选择表单，用户只能选择目录：

`zenity --file-selection --directory`

- 显示一个进度条，每秒更新其消息并显示进度百分比：

`{{(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")}} | zenity --progress`