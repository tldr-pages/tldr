# cupstestppd

> 测试 PPD 文件是否符合第 4.3 版规范。
> 错误代码（分别是 1, 2, 3, 4）：CLI 参数错误，无法打开文件，无法跳过的格式错误和不符合 PPD 规范。
> 注意：此命令已废弃。
> 参见：`lpadmin`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-cupstestppd.html>。

- 在安静模式下测试一个或多个文件的符合性：

`cupstestppd -q {{path/to/file1.ppd path/to/file2.ppd ...}}`

- 从 `stdin` 获取 PPD 文件，显示详细的符合性测试结果：

`cupstestppd -v - < {{path/to/file.ppd}}`

- 测试当前目录下所有 PPD 文件，打印出不符合规范的每个文件的名称：

`find . -name \*.ppd \! -execdir cupstestppd -q '{}' \; -print`
