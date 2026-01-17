# arp

> Tampilkan dan manipulasi cache informasi ARP pada sistem operasi Anda.
> Informasi lebih lanjut: <https://manned.org/arp.8>.

- Tampilkan informasi tabel ARP yang dikenali sistem operasi Anda saat ini:

`arp`

- Tampilkan tabel ARP dalam format [a]lternatif, gaya BSD dengan panjang kolom tetap:

`arp -a`

- Hapus ([d]elete) suatu entri dari tabel ARP sistem:

`sudo arp -d {{alamat_ip}}`

- [s]etel suatu entri baru ke dalam tabel ARP sistem:

`arp -s {{alamat_ip}} {{alamat_mac}}`
