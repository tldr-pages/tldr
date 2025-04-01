# bully

> 暴力破解无线接入点的 WPS PIN。
> 在使用 `bully` 之前，必须使用 `airmon-ng` 和 `airodump-ng` 收集必要的信息。
> 更多信息：<https://salsa.debian.org/pkg-security-team/bully>.

- 破解密码：

`bully --bssid "{{mac}}" --channel "{{channel}}" --bruteforce "{{interface}}"`

- 显示帮助：

`bully --help`