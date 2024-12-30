# airodump-ng

> 捕获数据包并显示有关无线网络的信息。
> 属于 `aircrack-ng`。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=airodump-ng>。

- 捕获数据包并显示有关 2.4GHz 频段无线网络的信息：

`sudo airodump-ng {{interface}}`

- 捕获数据包并显示有关 5GHz 频段无线网络的信息：

`sudo airodump-ng {{interface}} --band a`

- 捕获数据包并显示有关 2.4GHz 和 5GHz 频段无线网络的信息：

`sudo airodump-ng {{interface}} --band abg`

- 根据 MAC 地址和频道捕获数据包并显示有关无线网络的信息，并将输出保存到文件中：

`sudo airodump-ng --channel {{channel}} --write {{path/to/file}} --bssid {{mac}} {{interface}}`