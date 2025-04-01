# tuc

> 在分隔符匹配时切割文本（或字节），然后保留所需的部分。
> 这是 `cut` 的更易用和强大的版本，带有合理的默认设置。
> 更多信息：<https://github.com/riquito/tuc>.

- 切割并重新排列字段：

`echo "foo bar baz" | tuc -d '{{ }}' -f {{3,2,1}}`

- 将分隔符 `空格` 替换为箭头：

`echo "foo bar baz" | tuc -d ' ' -r ' ➡ '`

- 保留字段范围：

`echo "foo bar    baz" | tuc -d ' ' -f {{2:}}`

- 使用正则表达式切割：

`echo "a,b, c" | tuc -e '{{[, ]+}}' -f {{1,3}}`

- 输出 JSON 格式：

`echo "foo bar baz" | tuc -d '{{ }}' --json`
