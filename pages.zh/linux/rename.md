# rename

> 批量重命名文件。
> 注意：此页面指的是 `util-linux` 包中的命令。
> 对于 Perl 版本，请参见 `file-rename` 或 `perl-rename`。
> 警告：此命令没有保护措施，会不提示覆盖文件。
> 更多信息：<https://manned.org/rename>.

- 使用简单的替换重命名文件（将 'foo' 替换为 'bar'）：

`rename {{foo}} {{bar}} {{*}}`

- 模拟运行 - 显示哪些文件会被重命名但不实际执行：

`rename {{[-vn|--verbose --no-act]}} {{foo}} {{bar}} {{*}}`

- 不覆盖已存在的文件：

`rename {{[-o|--no-overwrite]}} {{foo}} {{bar}} {{*}}`

- 更改文件扩展名：

`rename {{.ext}} {{.bak}} {{*.ext}}`

- 在当前目录中的所有文件名前添加 "foo"：

`rename {{''}} {{'foo'}} {{*}}`

- 将一组编号递增的文件名中的数字补零到 3 位：

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
