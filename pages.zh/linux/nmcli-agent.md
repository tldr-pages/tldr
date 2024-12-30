# nmcli 代理

> 以 NetworkManager 秘密代理或 polkit 代理身份运行 `nmcli`。
> 此子命令也可以使用 `nmcli a` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>。

- 注册 `nmcli` 作为秘密代理并监听秘密请求：

`nmcli agent secret`

- 注册 `nmcli` 作为 polkit 代理并监听授权请求：

`nmcli agent polkit`

- 注册 `nmcli` 作为秘密代理和 polkit 代理：

`nmcli agent all`