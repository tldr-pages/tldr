# cupstestppd

> 测试PPD文件是否符合版本4.3的规范。
> 错误代码（分别为1、2、3和4）：错误的CLI参数，无法打开文件，无法跳过的格式错误和不符合PPD规范。
> 注意：此命令已被弃用。
> 另请参见：`lpadmin`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-cupstestppd.html>。

- 在静默模式下测试一个或多个文件的符合性：

`cupstestppd -q {{path/to/file1.ppd path/to/file2.ppd ...}}`

- 从`stdin`获取PPD文件，显示详细的符合性测试结果：

`cupstestppd -v - < {{path/to/file.ppd}}`

- 测试当前目录下的所有PPD文件，打印每个不符合的文件的名称：

`find . -name \*.ppd \! -execdir cupstestppd -q '{}' \; -print`