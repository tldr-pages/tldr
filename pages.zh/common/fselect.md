# fselect

> 使用 SQL 类似的查询来查找文件。
> 更多信息：<https://github.com/jhspetersson/fselect>。

- 从指定目录中选择临时文件或配置文件的完整路径和大小：

`fselect size, path from {{path/to/directory}} where name = {{'*.cfg'}} or name = {{'*.tmp'}}`

- 查找正方形图像：

`fselect path from {{path/to/directory}} where width = height`

- 查找老式说唱音乐 320kbps 的 MP3 文件：

`fselect path from {{path/to/directory}} where genre = {{Rap}} and bitrate = {{320}} and mp3_year lt {{2000}}`

- 仅选择前 5 个结果并以 JSON 格式输出：

`fselect size, path from {{path/to/directory}} limit {{5}} into json`

- 使用 SQL 聚合函数计算目录中文件的最小、最大和平均大小：

`fselect "{{MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)}} from {{path/to/directory}}"`
