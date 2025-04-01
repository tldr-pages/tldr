# docker commit

> 从容器的更改中创建新的镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/commit/>.

- 从特定容器创建镜像：

`docker commit {{container}} {{image}}:{{tag}}`

- 为创建的镜像应用 `CMD` Dockerfile 指令：

`docker commit --change "CMD {{command}}" {{container}} {{image}}:{{tag}}`

- 为创建的镜像应用 `ENV` Dockerfile 指令：

`docker commit --change "ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- 创建具有特定作者信息元数据的镜像：

`docker commit --author "{{author}}" {{container}} {{image}}:{{tag}}`

- 创建具有特定注释信息元数据的镜像：

`docker commit --message "{{comment}}" {{container}} {{image}}:{{tag}}`

- 创建镜像时不暂停容器：

`docker commit --pause {{false}} {{container}} {{image}}:{{tag}}`

- 显示帮助信息：

`docker commit --help`