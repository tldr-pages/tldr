# vinmap

> 一个多线程的Nmap扫描器，将IP范围分成块，执行并行扫描，并合并XML或JSON结果。
> 更多信息： <https://pypi.org/project/vinmap>。

- 执行子网的基本扫描：

`vinmap -ip {{192.168.1.0/24}}`

- 扫描一个域名，进行版本和操作系统检测，将结果保存到特定文件：

`vinmap -ip {{example.com}} -s "-sV -O" -o {{path/to/scan_results.xml}}`

- 使用10个块和20个并发线程扫描一个IP范围，如果未指定，将使用系统CPU核心的一半：

`vinmap -ip {{10.0.0.1-10.0.0.255}} -n 10 -t 20`

- 以JSON格式输出扫描结果：

`vinmap -ip {{192.168.1.1-192.168.1.100}} -f json`

- 使用默认设置扫描多个IP并保存合并的XML输出：

`vinmap -ip {{192.168.1.1,192.168.1.2,...}}`