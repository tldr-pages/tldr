# ack

> 一个类似grep的搜索工具，为程序员优化.

- 寻找包含"foo"的文件:

`ack {{foo}}`

- 在给定的语言中寻找文件:

`ack --ruby {{each_with_object}}`

- 计算匹配到"foo"的总次数:

`ack -ch {{foo}}`

- 列出内容包含"foo"的文件的文件名,并显示在每个文件中匹配的次数:

`ack -cl {{foo}}`
