# stressapptest

> 用户空间内存和IO测试。
> 更多信息：<https://github.com/stressapptest/stressapptest>。

- 测试给定数量的内存（以兆字节为单位）：

`stressapptest -M {{memory}}`

- 测试内存以及指定文件的I/O：

`stressapptest -M {{memory}} -f {{path/to/file}}`

- 测试指定的详细程度，其中0=最低，20=最高，8=默认：

`stressapptest -M {{memory}} -v {{level}}`