# 盒子

> 绘制、移除和修复 ASCII 艺术盒子。
> 更多信息：<https://boxes.thomasjensen.com/boxes-man-1.html>。

- 绕字符串绘制一个盒子：

`echo "{{string}}" | boxes`

- [r]emove 从字符串中移除一个盒子：

`echo "{{string}}" | boxes -r`

- 指定盒子 [d]esign：

`echo "{{string}}" | boxes -d {{parchment}}`

- 指定盒子 [s]ize（以列和行为单位）：

`echo "{{string}}" | boxes -s {{10}}x{{5}}`

- [a]lign 盒子文本 [h]orizontally（在 [l]eft、[c]enter 或 [r]ight）：

`echo "{{string}}" | boxes -a h{{l|c|r}}`

- [a]lign 盒子文本 [v]ertically（在 [t]op、[c]enter 或 [b]ottom）：

`echo "{{string}}" | boxes -a v{{t|c|b}}`

- [j]ustify 盒子文本（在 [l]eft、[c]enter 或 [r]ight）：

`echo "{{string}}" | boxes -a j{{l|c|r}}{{vt}}`