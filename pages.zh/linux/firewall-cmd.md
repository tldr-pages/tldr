# firewall-cmd

> firewalld 命令行客户端。
> 查看和调整运行时或永久防火墙配置状态。
> 更多信息：<https://firewalld.org/documentation/man-pages/firewall-cmd>。

- 查看运行时配置状态下所有可用的防火墙区域和规则：

`firewall-cmd --list-all-zones`

- 将接口永久移动到阻止区域，有效地阻止所有通信：

`firewall-cmd --permanent --zone={{block}} --change-interface={{enp1s0}}`

- 在指定区域永久打开服务的端口（如在 `public` 区域时的 443 端口）：

`firewall-cmd --permanent --zone={{public}} --add-service={{https}}`

- 在指定区域永久关闭服务的端口（如在 `public` 区域时的 80 端口）：

`firewall-cmd --permanent --zone={{public}} --remove-service={{http}}`

- 在指定区域永久转发传入数据包的端口（如将 443 端口转发到 8443，当进入 `public` 区域时）：

`firewall-cmd --permanent --zone={{public}} --add-rich-rule='rule family="{{ipv4|ipv6}}" forward-port port="{{443}}" protocol="{{udp|tcp}}" to-port="{{8443}}"'`

- 重新加载 firewalld，以丢失任何运行时更改并强制永久配置立即生效：

`firewall-cmd --reload`

- 将运行时配置状态保存到永久配置中：

`firewall-cmd --runtime-to-permanent`

- 在紧急情况下启用恐慌模式。所有流量将被丢弃，任何活动连接将被终止：

`firewall-cmd --panic-on`