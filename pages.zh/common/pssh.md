# pssh

> 并行 SSH 程序。
> 更多信息：<https://manned.org/pssh>。

- 在两台主机上运行命令，并在每台服务器上按行打印输出：

`pssh -i -H "{{host1}} {{host2}}" {{hostname -i}}`

- 运行命令并将输出保存到不同的文件中：

`pssh -H {{host1}} -H {{host2}} -o {{path/to/output_dir}} {{hostname -i}}`

- 从一个以换行符分隔的文件中指定多个主机并运行命令：

`pssh -i -h {{path/to/hosts_file}} {{hostname -i}}`

- 以 root 用户身份运行命令（这将要求输入 root 密码）：

`pssh -i -h {{path/to/hosts_file}} -A -l {{root_username}} {{hostname -i}}`

- 使用额外的 SSH 参数运行命令：

`pssh -i -h {{path/to/hosts_file}} -x "{{-O VisualHostKey=yes}}" {{hostname -i}}`

- 限制并发连接数为 10 并运行命令：

`pssh -i -h {{path/to/hosts_file}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`
