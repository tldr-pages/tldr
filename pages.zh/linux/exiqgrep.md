# exiqgrep

> Perl 脚本，提供在 Exim 队列输出中使用 `grep` 的功能。
> 更多信息：<https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>.

- 使用不区分大小写的搜索匹配发件人地址：

`exiqgrep -f '<{{email@somedomain.com}}>'`

- 匹配发件人地址并仅显示邮件 ID：

`exiqgrep -i -f '<{{email@somedomain.com}}>'`

- 匹配收件人地址：

`exiqgrep -r '{{email@somedomain.com}}'`

- 从队列中删除所有匹配发件人地址的邮件：

`exiqgrep -i -f '<{{email@somedomain.com}}>' | xargs exim -Mrm`

- 测试退信邮件：

`exiqgrep -f '^<>$'`

- 显示退信邮件的数量：

`exiqgrep -c -f '^<>$'`
