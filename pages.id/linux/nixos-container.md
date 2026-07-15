# nixos-container

> Jalankan kumpulan kontainer NixOS menggunakan sistem kontainer Linux.
> Informasi lebih lanjut: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- Tampilkan daftar kontainer yang sedang berjalan:

`sudo nixos-container list`

- Buat suatu kontainer NixOS menggunakan berkas konfigurasi tertentu

`sudo nixos-container create {{nama_kontainer}} --config-file {{jalan/menuju/berkas_konfigurasi_nix}}`

- Jalankan, hentikan, matikan, hancurkan, atau tampilkan kondisi suatu kontainer:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{nama_kontainer}}`

- Jalankan sebuah perintah dalam suatu kontainer berjalan:

`sudo nixos-container run {{nama_kontainer}} -- {{perintah}} {{argumen_perintah}}`

- Perbarui konfigurasi suatu kontainer:

`sudo $EDITOR /var/lib/container/{{nama_kontainer}}/etc/nixos/configuration.nix && sudo nixos-container update {{nama_kontainer}}`

- Masuk ke dalam sesi shell interaktif baru dalam suatu kontainer berjalan:

`sudo nixos-container root-login {{nama_kontainer}}`
