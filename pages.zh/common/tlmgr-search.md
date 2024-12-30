# tlmgr 搜索

> 使用 (Perl) 正则表达式搜索 TeX Live 包。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 从特定的正则表达式中搜索所有本地安装包的包名和描述：

`tlmgr search "{{regular_expression}}"`

- 从正则表达式中搜索所有本地安装包的所有文件名：

`tlmgr search --file "{{regular_expression}}"`

- 从正则表达式中搜索所有本地安装包的所有文件名、包名和描述：

`tlmgr search --all "{{regular_expression}}"`

- 搜索 TeX Live 数据库，而不是本地安装：

`tlmgr search --global "{{regular_expression}}"`

- 将包名和描述的匹配限制为完整单词（但不包括文件名）：

`tlmgr search --all --word "{{regular_expression}}"`