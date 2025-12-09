# arp

> Tampilkan dan manipulasi cache informasi ARP pada sistem operasi Anda.
> Informasi lebih lanjut: <https://manned.org/arp.8>.

- Tampilkan informasi tabel ARP yang dikenali sistem operasi Anda saat ini:

`arp -a`

- Hapus suatu entri dari tabel ARP sistem:

`arp -d {{alamat}}`

- Ma[s]ukkan suatu entri baru ke dalam tabel ARP sistem:

`arp -s {{alamat_ip}} {{alamat_mac}}`
