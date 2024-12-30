# 路由

> 手动操作路由表。
> 需要根权限。
> 更多信息：<https://keith.github.io/xcode-man-pages/route.8.html>。

- 通过网关添加到目的地的路由：

`sudo route add "{{destination_ip_address}}" "{{gateway_address}}"`

- 通过网关添加到 /24 子网的路由：

`sudo route add "{{subnet_ip_address}}/24" "{{gateway_address}}"`

- 以测试模式运行（不执行任何操作，只打印）：

`sudo route -t add "{{destination_ip_address}}/24" "{{gateway_address}}"`

- 删除所有路由：

`sudo route flush`

- 删除特定路由：

`sudo route delete "{{destination_ip_address}}/24"`

- 查找并显示目的地的路由（主机名或IP地址）：

`sudo route get "{{destination}}"`