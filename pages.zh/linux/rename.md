# 重命名

> 重命名多个文件。
> 注意：本页面提到的是来自 `util-linux` 软件包的命令。
> 对于 Perl 版本，请参见 `file-rename` 或 `perl-rename`。
> 警告：此命令没有任何保护措施，会在不提示的情况下覆盖文件。
> 更多信息：<https://manned.org/rename>。

- 使用简单替换重命名文件（将找到的 'foo' 替换为 'bar'）：

`rename {{foo}} {{bar}} {{*}}`

- 演练 - 显示将会发生的重命名，而不实际执行：

`rename -vn {{foo}} {{bar}} {{*}}`

- 不覆盖现有文件：

`rename -o {{foo}} {{bar}} {{*}}`

- 更改文件扩展名：

`rename {{.ext}} {{.bak}} {{*.ext}}`

- 在当前目录中的所有文件名前加上 "foo"：

`rename {{''}} {{'foo'}} {{*}}`

- 对一组编号逐渐增加的文件进行重命名，数字补零到三位数：

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`