# aireplay-ng

> 向无线网络注入数据包。
> `aircrack-ng` 的一部分。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- 向指定的接入点（AP）MAC 地址、客户端 MAC 地址和接口发送指定数量的去关联（disassociate）数据包：

`sudo aireplay-ng --deauth {{count}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}}`
