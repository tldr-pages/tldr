# aireplay-ng

> 무선 네트워크에 패킷을 주입.
> `aircrack-ng`의 일부.
> 더 많은 정보: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- 액세스 포인트의 MAC 주소, 클라이언트의 MAC 주소 및 인터페이스가 주어지면, 특정 개수의 분리된 패킷을 전송:

`sudo aireplay-ng --deauth {{count}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}}`
