# avahi-resolve

> 在主机名和IP地址之间进行转换。
> 更多信息：<https://www.avahi.org/>.

- 将本地服务解析为其IPv4：

`avahi-resolve -4 --name {{service.local}}`

- 将IP解析为主机名，详细输出：

`avahi-resolve --verbose --address {{IP}}`