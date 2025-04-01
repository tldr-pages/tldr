# tlmgr search

> 使用（Perl）正则表达式搜索 TeX Live 包。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 使用特定的正则表达式搜索本地已安装包的名称和描述：

`tlmgr search "{{regular_expression}}"`

- 使用正则表达式搜索本地已安装所有包的所有文件名：

`tlmgr search --file "{{regular_expression}}"`

- 使用正则表达式搜索本地已安装所有包的所有文件名、包名和描述：

`tlmgr search --all "{{regular_expression}}"`

- 搜索 TeX Live 数据库，而不是本地安装：

`tlmgr search --global "{{regular_expression}}"`

- 将包名和描述（但不包括文件名）的匹配限制为完整单词：

`tlmgr search --all --word "{{regular_expression}}"`
