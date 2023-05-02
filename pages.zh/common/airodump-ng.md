# airodump-ng

> 捕获数据包并显示有关无线网络的信息。
> `aircrack-ng` 的一部分。
> 更多信息： <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- 捕获数据包并显示有关无线网络的信息：

`sudo airodump-ng {{interface}}`

- 捕获数据包并显示有关无线网络的信息，给定 MAC 地址和信道，并将输出保存到文件中：

`sudo airodump-ng --channel {{信道}} --write {{路径/到/文件}} --bssid {{mac}} {{interface}}`
