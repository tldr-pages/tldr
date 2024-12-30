# docker commit

> 从容器的更改创建新镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/commit/>。

- 从特定容器创建镜像：

`docker commit {{container}} {{image}}:{{tag}}`

- 对创建的镜像应用 `CMD` Dockerfile 指令：

`docker commit --change "CMD {{command}}" {{container}} {{image}}:{{tag}}`

- 对创建的镜像应用 `ENV` Dockerfile 指令：

`docker commit --change "ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- 在元数据中创建带有特定作者的镜像：

`docker commit --author "{{author}}" {{container}} {{image}}:{{tag}}`

- 在元数据中创建带有特定注释的镜像：

`docker commit --message "{{comment}}" {{container}} {{image}}:{{tag}}`

- 在提交时不暂停容器创建镜像：

`docker commit --pause {{false}} {{container}} {{image}}:{{tag}}`

- 显示帮助信息：

`docker commit --help`