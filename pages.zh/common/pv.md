# pv

> 监控数据通过管道的进度。
> 更多信息：<https://manned.org/pv>。

- 打印文件内容并显示进度条：

`pv {{path/to/file}}`

- 测量管道之间的数据流速度和数量（`--size`是可选的）：

`command1 | pv --size {{expected_amount_of_data_for_eta}} | command2`

- 过滤文件，同时查看进度和输出数据的数量：

`pv -cN in {{big_text_file}} | grep {{pattern}} | pv -cN out > {{filtered_file}}`

- 附加到一个已经运行的进程并查看其文件读取进度：

`pv -d {{PID}}`

- 读取一个有错误的文件，跳过错误，就像`dd conv=sync,noerror`那样：

`pv -EE {{path/to/faulty_media}} > image.img`

- 在读取指定数量的数据后停止，限制速率为1K/s：

`pv -L 1K --stop-at --size {{maximum_file_size_to_be_read}}`