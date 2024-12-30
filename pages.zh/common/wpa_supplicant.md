# wpa_supplicant

> 管理受保护的无线网络。
> 更多信息：<https://manned.org/wpa_supplicant.1>。

- 加入受保护的无线网络：

`wpa_supplicant -i {{interface}} -c {{path/to/wpa_supplicant_conf.conf}}`

- 加入受保护的无线网络并以守护进程运行：

`wpa_supplicant -B -i {{interface}} -c {{path/to/wpa_supplicant_conf.conf}}`