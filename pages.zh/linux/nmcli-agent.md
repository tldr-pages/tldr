# nmcli agent

> 以 NetworkManager 密码代理或 polkit 代理的方式运行 `nmcli`。
> 此子命令也可以通过 `nmcli a` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>。

- 注册 `nmcli` 为密码代理并监听密码请求：

`nmcli agent secret`

- 注册 `nmcli` 为 polkit 代理并监听授权请求：

`nmcli agent polkit`

- 注册 `nmcli` 为密码代理和 polkit 代理：

`nmcli agent all`