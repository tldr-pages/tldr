# winword

> Microsoft Office 的文字处理应用程序。
> 更多信息：<https://support.microsoft.com/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6#category=word>。

- 启动文字处理应用程序：

`winword`

- 在不打开任何文档的情况下启动 Word：

`winword /n`

- 新建空白文档：

`winword /w`

- 基于现有文件创建新文档：

`winword /f {{path\to\file.docx}}`

- 打开一个或多个文件以进行编辑：

`winword /t {{path\to\file1.docx path\to\file2.docx ...}}`

- 打开文件并禁用所有 AutoExec 宏：

`winword /m {{path\to\file.docm}}`

- 打开文件并禁用所有 AutoExec 宏，然后运行指定的宏：

`winword /m{{MacroName}} {{path\to\file.docm}}`

- 以安全模式启动 Microsoft Word：

`winword /safe`
