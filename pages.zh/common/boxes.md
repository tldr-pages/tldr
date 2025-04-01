# boxes

> 绘制、移除和修复 ASCII 艺术框。
> 更多信息：<https://boxes.thomasjensen.com/boxes-man-1.html>.

- 在字符串周围绘制一个框：

`echo "{{string}}" | boxes`

- 从字符串中移除框：

`echo "{{string}}" | boxes {{[-r|--remove]}}`

- 指定框的设计：

`echo "{{string}}" | boxes {{[-d|--design]}} {{parchment}}`

- 指定框的大小（以列和行表示）：

`echo "{{string}}" | boxes {{[-s|--size]}} {{10}}x{{5}}`

- 水平对齐框中的文本（左对齐 [l]、居中 [c] 或右对齐 [r]）：

`echo "{{string}}" | boxes {{[-a|--align]}} h{{l|c|r}}`

- 垂直对齐框中的文本（顶部对齐 [t]、居中 [c] 或底部对齐 [b]）：

`echo "{{string}}" | boxes {{[-a|--align]}} v{{t|c|b}}`

- 对齐框中的文本（左对齐 [l]、居中 [c] 或右对齐 [r]）：

`echo "{{string}}" | boxes {{[-a|--align]}} j{{l|c|r}}{{vt}}`