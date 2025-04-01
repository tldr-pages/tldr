# stressapptest

> 用户空间内存和IO测试工具。
> 更多信息：<https://github.com/stressapptest/stressapptest>.

- 测试指定数量的内存（以兆字节为单位）：

`stressapptest -M {{memory}}`

- 测试内存及指定文件的I/O：

`stressapptest -M {{memory}} -f {{path/to/file}}`

- 指定详细程度级别进行测试，其中0=最低，20=最高，8=默认：

`stressapptest -M {{memory}} -v {{level}}`
