# pv

> 监控通过管道的数据进度。
> 更多信息: <https://manned.org/pv>.

- 打印文件内容并显示进度条：

`pv {{path/to/file}}`

- 测量管道之间数据流动的速度和数量（`--size` 为可选）：

`command1 | pv --size {{expected_amount_of_data_for_eta}} | command2`

- 过滤文件，同时查看进度和输出数据量：

`pv -cN in {{big_text_file}} | grep {{pattern}} | pv -cN out > {{filtered_file}}`

- 附加到一个已运行的进程并查看其文件读取进度：

`pv -d {{PID}}`

- 读取错误文件，跳过错误，如 `dd conv=sync,noerror` 所做：

`pv -EE {{path/to/faulty_media}} > image.img`

- 读取指定数量的数据后停止，速率限制为 1K/s：

`pv -L 1K --stop-at --size {{maximum_file_size_to_be_read}}`