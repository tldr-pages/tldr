# zenity

> 从命令行/Shell 脚本显示对话框。
> 返回用户输入的值或在发生错误时返回 1。
> 更多信息：<https://manned.org/zenity>。

- 显示默认的问题对话框：

`zenity --question`

- 显示一个包含文本 "Hello!" 的信息对话框：

`zenity --info --text="{{Hello!}}"`

- 显示一个姓名/密码表单，并以 ";" 分隔输出数据：

`zenity --forms --add-entry="{{Name}}" --add-password="{{Password}}" --separator="{{;}}"`

- 显示一个仅允许选择目录的文件选择对话框：

`zenity --file-selection --directory`

- 显示一个进度条，每秒更新一次消息并显示进度百分比：

`{{(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")}} | zenity --progress`
