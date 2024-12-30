# aireplay-ng

> 向无线网络注入数据包。
> 是 `aircrack-ng` 的一部分。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=aireplay-ng>。

- 发送特定数量的去关联数据包，给定接入点的 MAC 地址、客户端的 MAC 地址和接口：

`sudo aireplay-ng --deauth {{count}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}}`