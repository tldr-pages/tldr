# exiqgrep

> Perl 脚本，提供在 Exim 队列输出中使用 `grep` 的功能。
> 更多信息请访问：<https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>。

- 使用不区分大小写的搜索匹配发件人地址：

`exiqgrep -f '<{{email@somedomain.com}}>'`

- 匹配发件人地址并仅显示消息 ID：

`exiqgrep -i -f '<{{email@somedomain.com}}>'`

- 匹配收件人地址：

`exiqgrep -r '{{email@somedomain.com}}'`

- 从队列中移除所有匹配发件人地址的消息：

`exiqgrep -i -f '<{{email@somedomain.com}}>' | xargs exim -Mrm`

- 测试是否有退信消息：

`exiqgrep -f '^<>$'`

- 显示退信消息的数量：

`exiqgrep -c -f '^<>$'`