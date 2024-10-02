# fping

> Utilitas ping lebih kuat yang dapat melakukan proses ping pada lebih dari satu host.
> Informasi lebih lanjut: <https://fping.org>.

- Tampilkan daftar seluruh host yang aktif dalam suatu subjaringan menurut definisi network mask (netmask):

`fping {{-a|--alive}} {{-g|--generate}} 192.168.1.0/24`

- Tampilkan daftar seluruh host yang aktif dalam suatu subjaringan berdasarkan rentang alamat IP:

`fping {{-a|--alive}} {{-g|--generate}} 192.168.1.1 192.168.1.254`

- Tampilkan daftar seluruh host yang tidak aktif dalam suatu subjaringan menurut definisi network mask (netmask):

`fping {{-u|--unreach}} {{-g|--generate}} 192.168.1.0/24`
