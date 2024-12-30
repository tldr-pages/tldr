# fselect

> 使用类似SQL的查询查找文件。
> 更多信息请访问: <https://github.com/jhspetersson/fselect>。

- 从给定目录中的临时文件或配置文件中选择完整路径和大小：

`fselect size, path from {{path/to/directory}} where name = {{'*.cfg'}} or name = {{'*.tmp'}}`

- 查找正方形图片：

`fselect path from {{path/to/directory}} where width = height`

- 查找老派嘻哈音乐320kbps的MP3文件：

`fselect path from {{path/to/directory}} where genre = {{Rap}} and bitrate = {{320}} and mp3_year lt {{2000}}`

- 仅选择前5个结果并以JSON格式输出：

`fselect size, path from {{path/to/directory}} limit {{5}} into json`

- 使用SQL聚合函数计算目录中文件的最小、最大和平均大小：

`fselect "{{MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)}} from {{path/to/directory}}"`