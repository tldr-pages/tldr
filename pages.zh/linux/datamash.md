# datamash

> 对输入的文本数据文件执行基本的数值、文本和统计操作。
> 更多信息：<https://www.gnu.org/software/datamash/manual/html_node/Invoking-datamash.html>.

- 获取单列数字的最大值、最小值、平均值和中位数：

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- 获取单列浮点数的平均值（浮点数必须使用","而不是"."）：

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- 获取单列数字的平均值，并指定小数位数：

`echo -e '1\n2\n3\n4\n5\n5' | datamash {{[-R|--round]}} {{wanted_number_of_decimals}} mean 1`

- 获取单列数字的平均值，忽略"Na"和"NaN"（字面字符串）：

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
