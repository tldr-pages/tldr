# ar

> 创建, 修改, 提取库文件 (.a, .so, .o).

- 从库文件中提取全部成员:

`ar -x {{libfoo.a}}`

- 列出库文件中的成员:

`ar -t {{libfoo.a}}`

- 替换或添加文件到库文件:

`ar -r {{libfoo.a}} {{foo.o}} {{bar.o}} {{baz.o}}`

- 插入对象文件索引（相当于使用`ranlib`):

`ar -s {{libfoo.a}}`

- 使用文件和附带的目标文件索引创建存档:

`ar -rs {{libfoo.a}} {{foo.o}} {{bar.o}} {{baz.o}}`
