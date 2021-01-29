# rsync

> 一种快速，通用，远程（和本地）文件复制工具
> 更多信息：<https://linux.die.net/man/1/rsync>

- 从本地传输文件到远程主机：

`rsync {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- 从远程主机传输文件到本地：

`rsync {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- 将本地文件以归档（-a）模式并保留几乎所有属性，同时使用压缩（-z）功能传输到远程主机，并以人类可读方式（-h）输出详细信息（-v）和进度条（-P）：

`rsync -azvhP {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- 将远程主机目录上的所有文件，以递归模式传输到本地：

`rsync -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- 将远程主机该目录下的所有内容（不包含该目录），以递归方式传输到本地：

`rsync -r {{remote_host}}:{{path/to/remote_directory}}/ {{path/to/local_directory}}`

- 递归方式（-r）传输目录，保留几乎所有属性（-a），解析软连接（-L），并忽略已传输的文件（-u）：

`rsync -rauL {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- 指定本地和远程之间通信方式（-e），删除本地有而远程主机没有的文件，只对将要同步的目录生效（--delete）：

`rsync -e ssh --delete {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`

- 指定本地和远程之间通信方式（-e），使用指定端口，显示进度条：

`rsync -e 'ssh -p {{port}}' -P {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`

