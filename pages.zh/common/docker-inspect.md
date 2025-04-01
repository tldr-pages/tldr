# docker inspect

> 返回 Docker 对象的低级信息。
> 更多信息： <https://docs.docker.com/reference/cli/docker/inspect/>.

- 显示帮助：

`docker inspect`

- 使用名称或 ID 显示容器、镜像或卷的信息：

`docker inspect {{container|image|ID}}`

- 显示容器的 IP 地址：

`docker inspect --format '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{container}}`

- 显示容器日志文件的路径：

`docker inspect --format='\{\{.LogPath\}\}' {{container}}`

- 显示容器的镜像名称：

`docker inspect --format='\{\{.Config.Image\}\}' {{container}}`

- 以 JSON 格式显示配置信息：

`docker inspect --format='\{\{json .Config\}\}' {{container}}`

- 显示所有端口映射：

`docker inspect --format='\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{container}}`
