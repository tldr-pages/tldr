# perl

> Perl 5 语言解释器。
> 更多信息：<https://www.perl.org>。

- 从 `stdin` 打印匹配 regex1 和不区分大小写 [/i] 的 regex2 的行：

`perl -n -e 'print if m/{{regex1}}/ and m/{{regex2}}/i'`

- 使用正则表达式，忽略正则中的空格 [/x]，打印第一个匹配组 [-E]：

`perl -n -E 'say $1 if m/{{before}} (  {{group_regex}}  ) {{after}}/x'`

- 原地 [-i] 替换，并备份，替换所有出现的正则表达式 [/g]：

`perl -i'.bak' -p -e 's/{{regex}}/{{replacement}}/g' {{path/to/files}}`

- 使用 Perl 的内联文档，部分页面也可通过 Linux 手册页查看：

`perldoc perlrun ; perldoc module ; perldoc -f splice; perldoc -q perlfaq1`