# arping

> Cari dan selidiki para host jaringan melalui protokol ARP.
> Bermanfaat untuk mencari alamat MAC dalam jaringan.
> Informasi lebih lanjut: <https://manned.org/arping>.

- Ping suatu host dengan megirimkan paket permintaan ARP:

`sudo arping {{alamat_ip_host}}`

- Ping suatu host melalui antarmuka jaringan tertentu (contoh: `eth0`):

`sudo arping -I {{antarmuka_jaringan}} {{alamat_ip_host}}`

- Ping suatu host dan hentikan jika sang host mulai membalasnya:

`sudo arping -f {{alamat_ip_host}}`

- Ping suatu host untuk jumlah kesempatan tertentu:

`sudo arping -c {{jumlah_kesempatan}} {{alamat_ip_host}}`

- Sebarluaskan paket permintaan ARP kepada host apapun untuk membantu memutakhirkan informasi ARP dalam host tetangga:

`sudo arping -U {{alamat_ip_untuk_disebarluaskan}}`

- [D]eteksi adanya alamat IP duplikat dalam jaringan ini dengan mengirimkan permintaan ARP dengan jangka waktu habis (timeout) sebanyak 3 detik:

`sudo arping -D -w {{3}} {{alamat_ip_untuk_diperiksa}}`
