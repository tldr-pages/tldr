# mutagen

> 实时文件同步和网络转发工具。
> 更多信息：<https://mutagen.io>.

- 在本地目录和远程主机之间启动同步会话：

`mutagen sync create --name={{session_name}} {{/path/to/local/directory/}} {{user}}@{{host}}:{{/path/to/remote/directory/}}`

- 在本地目录和 Docker 容器之间启动同步会话：

`mutagen sync create --name={{session_name}} {{/path/to/local/directory/}} docker://{{user}}@{{container_name}}{{/path/to/remote/directory/}}`

- 停止一个正在运行的会话：

`mutagen sync terminate {{session_name}}`

- 启动一个项目：

`mutagen project start`

- 停止一个项目：

`mutagen project terminate`

- 列出当前项目的正在运行的会话：

`mutagen project list`
