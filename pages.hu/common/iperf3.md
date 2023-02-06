# iperf3

> Forgalomgenerátor a hálózati sávszélesség tesztelésére. További információ: <https://iperf.fr>.

- Az iperf3 futtatása szerverként:

`iperf3 -s`

- Futtasson iperf3 kiszolgálót egy adott porton:

`iperf3 -s -p {{port}}`

- Sávszélesség-teszt indítása:

`iperf3 -c {{server}}`

- Az iperf3 futtatása több párhuzamos folyamban:

`iperf3 -c {{server}} -P {{streams}}`

- A teszt irányának megfordítása. A kiszolgáló adatokat küld az ügyfélnek:

`iperf3 -c {{server}} -R`
