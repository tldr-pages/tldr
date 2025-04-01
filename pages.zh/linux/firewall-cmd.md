# firewall-cmd

> firewalld 命令行客户端。
> 查看和调整运行时或永久的防火墙配置状态。
> 更多信息：<https://firewalld.org/documentation/man-pages/firewall-cmd>。

- 查看所有可用的防火墙区域及其规则的运行时配置状态：

`firewall-cmd --list-all-zones`

- 永久将接口移至阻塞区域，有效阻止所有通信：

`firewall-cmd --permanent --zone={{block}} --change-interface={{enp1s0}}`

- 在指定区域永久打开服务的端口（例如在 `public` 区域开放 443 端口）：

`firewall-cmd --permanent --zone={{public}} --add-service={{https}}`

- 在指定区域永久关闭服务的端口（例如在 `public` 区域关闭 80 端口）：

`firewall-cmd --permanent --zone={{public}} --remove-service={{http}}`

- 在指定区域永久转发入站数据包的端口（例如将进入 `public` 区域的 443 端口转发到 8443 端口）：

`firewall-cmd --permanent --zone={{public}} --add-rich-rule='rule family="{{ipv4|ipv6}}" forward-port port="{{443}}" protocol="{{udp|tcp}}" to-port="{{8443}}"'`

- 重新加载 firewalld 以丢弃所有运行时更改并立即应用永久配置：

`firewall-cmd --reload`

- 将运行时配置状态保存到永久配置：

`firewall-cmd --runtime-to-permanent`

- 在紧急情况下启用应急模式。所有流量将被丢弃，任何活动连接将被终止：

`firewall-cmd --panic-on`
