# perl

> Perl 5语言解释器。
> 更多信息：<https://www.perl.org>。

- 从 `stdin` 打印与正则表达式 regex1 匹配且不区分大小写的 regex2 的行：

`perl -n -e 'print if m/{{regex1}}/ and m/{{regex2}}/i'`

- 使用正则表达式 [-E] 输出第一个匹配组，忽略正则表达式中的空格 [/x]：

`perl -n -E 'say $1 if m/{{before}} (  {{group_regex}}  ) {{after}}/x'`

- [-i] 就地编辑，带备份， [/s] 将所有匹配正则表达式的发生 [/g] 替换为替代内容：

`perl -i'.bak' -p -e 's/{{regex}}/{{replacement}}/g' {{path/to/files}}`

- 使用 Perl 的内联文档，有些页面在 Linux 上也可通过手册页访问：

`perldoc perlrun ; perldoc module ; perldoc -f splice; perldoc -q perlfaq1`