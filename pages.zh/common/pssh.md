# pssh

> 并行SSH程序。
> 更多信息：<https://manned.org/pssh>。

- 在两个主机上运行命令，并在线打印每个服务器的输出：

`pssh -i -H "{{host1}} {{host2}}" {{hostname -i}}`

- 运行命令并将输出保存到不同的文件中：

`pssh -H {{host1}} -H {{host2}} -o {{path/to/output_dir}} {{hostname -i}}`

- 在多个主机上运行命令，主机在一个换行分隔的文件中指定：

`pssh -i -h {{path/to/hosts_file}} {{hostname -i}}`

- 以root身份运行命令（这要求输入root密码）：

`pssh -i -h {{path/to/hosts_file}} -A -l {{root_username}} {{hostname -i}}`

- 运行命令时添加额外的SSH参数：

`pssh -i -h {{path/to/hosts_file}} -x "{{-O VisualHostKey=yes}}" {{hostname -i}}`

- 运行命令并将并行连接数限制为10：

`pssh -i -h {{path/to/hosts_file}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`