# rsync

> 一种快速，通用，远程（和本地）文件复制工具。
> 更多信息：<https://download.samba.org/pub/rsync/rsync.1>.

- 从本地传输文件到远程主机：

`rsync {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- 从远程主机传输文件到本地：

`rsync {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- 将本地文件以归档模式并保留几乎所有属性，同时使用压缩功能传输到远程主机，并以人类可读方式输出详细信息和进度条：

`rsync --archive --compress --verbose --human-readable --progress {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- 将远程主机目录上的所有文件，以递归模式传输到本地：

`rsync --recursive {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- 将远程主机该目录下的所有内容（不包含该目录），以递归方式传输到本地：

`rsync --recursive {{remote_host}}:{{path/to/remote_directory}}/ {{path/to/local_directory}}`

- 递归方式传输目录，保留几乎所有属性，解析软连接，并忽略已传输的文件：

`rsync --recursive --archive --update --copy-links {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- 指定本地和远程之间通信方式：

`rsync --rsh ssh {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`

- 指定本地和远程之间通信方式，使用指定端口，并显示进度条：

`rsync --rsh 'ssh -p {{port}}' --progress {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`
