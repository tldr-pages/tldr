# arp-scan

> Kirim paket ARP menuju kumpulan alamat IP atau host untuk memindai suatu jaringan komputer lokal.
> Informasi lebih lanjut: <https://github.com/royhills/arp-scan>.

- Pindai jaringan lokal yang terhubung saat ini:

`arp-scan --localnet`

- Pindai suatu alamat IP dengan pengaturan bitmask khusus:

`arp-scan {{192.168.1.1}}/{{24}}`

- Pindai suatu jaringan IP menggunakan rentang alamat tertentu:

`arp-scan {{172.0.0.0}}-{{127.0.0.31}}`

- Pindai suatu jaringan IP menggunakan net mask khusus:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`
