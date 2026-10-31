# ufw

> Uncomplicated Firewall.
> Antarmuka untuk `iptables` yang bertujuan mempermudah konfigurasi firewall.
> Beberapa subperintah seperti `allow`, `enable`, `delete`, dll. memiliki dokumentasi penggunaannya sendiri.
> Informasi lebih lanjut: <https://manned.org/ufw>.

- Aktifkan/Nonaktifkan `ufw`:

`sudo ufw {{enable|disable}}`

- Tampilkan aturan `ufw` beserta nomor urutnya:

`sudo ufw status numbered`

- Izinkan lalu lintas masuk pada port 5432 beserta komentar identifikasi layanan:

`sudo ufw allow 5432 comment "{{Layanan}}"`

- Izinkan hanya lalu lintas TCP dari 192.168.0.4 ke alamat mana pun pada host ini, pada port 22:

`sudo ufw allow proto tcp from 192.168.0.4 to any port 22`

- Izinkan lalu lintas dari IP mana pun pada subnet 192.168.0.0/24 melalui port 53, hanya pada antarmuka eth0:

`sudo ufw allow in on eth0 from 192.168.0.0/24 to any port 53`

- Blokir lalu lintas pada port 80 pada host ini:

`sudo ufw deny 80`

- Blokir semua lalu lintas UDP ke rentang port 8412:8500:

`sudo ufw deny proto udp from any to any port 8412:8500`

- Hapus aturan tertentu (nomor aturan dapat diperoleh dari perintah `ufw status numbered`):

`sudo ufw delete {{nomor_aturan}}`
