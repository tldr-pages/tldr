# pw-config

> 列出将被 PipeWire 服务器和客户端使用的配置路径和部分。
> 更多信息：<https://docs.pipewire.org/page_man_pw-config_1.html>。

- 列出所有将被使用的配置文件：

`pw-config`

- 列出 PipeWire PulseAudio 服务器将使用的所有配置文件：

`pw-config --name pipewire-pulse.conf`

- 列出 PipeWire PulseAudio 服务器使用的所有配置部分：

`pw-config --name pipewire-pulse.conf list`

- 列出 JACK 客户端使用的 `context.properties` 片段：

`pw-config --name jack.conf list context.properties`

- 列出 JACK 客户端使用的合并 `context.properties`：

`pw-config --name jack.conf merge context.properties`

- 列出 PipeWire 服务器使用的合并 `context.modules` 并进行 [r]eformat：

`pw-config --name pipewire.conf --recurse merge context.modules`

- 显示帮助：

`pw-config --help`