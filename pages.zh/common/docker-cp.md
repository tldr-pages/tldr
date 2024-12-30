# docker cp

> 在主机和容器文件系统之间复制文件或目录。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/cp/>

- 从主机复制文件或目录到容器：

`docker cp {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`

- 从容器复制文件或目录到主机：

`docker cp {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}`

- 从主机复制文件或目录到容器，跟随符号链接（直接复制符号链接指向的文件，而不是符号链接本身）：

`docker cp --follow-link {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`