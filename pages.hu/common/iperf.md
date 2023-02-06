# iperf

> A számítógépek közötti hálózati sávszélesség mérése. További információ: <https://iperf.fr>.

- Kiszolgálón futtatható:

`iperf -s`

- Futtassa a szerveren UDP módban, és állítsa be a szerver portját úgy, hogy az 5001-es porton figyeljen:

`iperf -u -s -p {{5001}}`

- Futtatás az ügyfeleken:

`iperf -c {{server_address}}`

- Futtatás az ügyfélre 2 másodpercenként:

`iperf -c {{server_address}} -i {{2}}`

- Futtatás kliensen 5 párhuzamos szálakkal:

`iperf -c {{server_address}} -P {{5}}`

- Futtatás az ügyfeleken UDP módban:

`iperf -u -c {{server_address}} -p {{5001}}`
