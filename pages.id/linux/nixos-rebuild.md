# nixos-rebuild

> Lakukan konfigurasi ulang bagi suatu mesin NixOS.
> Informasi lebih lanjut: <https://nixos.org/nixos/manual/#sec-changing-config>.

- Bangun dan pindah menuju sistem NixOS yang dibangun berdasarkan konfigurasi terbaru, sebagai pilihan sistem bawaan terbaru dalam proses boot:

`sudo nixos-rebuild switch`

- Bangun dan pindah sistem dengan nama baru yang ditentukan:

`sudo nixos-rebuild switch {{[-p|--profile-name]}} {{nama}}`

- Bangun dan pindah sistem dengan memutakhirkan seluruh paket piranti lunak di dalamnya:

`sudo nixos-rebuild switch --upgrade`

- Bangun dan pindah sistem dengan mengembalikan pemasangan seluruh paket piranti lunak ke dalam kondisi pra-mutakhir:

`sudo nixos-rebuild switch --rollback`

- Bangun sistem berdasarkan konfigurasi terbaru dan simpan sebagai bawaan baru proses boot tanpa memindahkan sesi saat ini kepadanya:

`sudo nixos-rebuild boot`

- Bangun dan pindah ke sistem baru dalam mode uji coba (tanpa menyimpannya sebagai entri sistem baru dalam proses boot):

`sudo nixos-rebuild test`

- Bangun dengan konfigurasi terbaru dan buka sistem terbaru dalam mesin virtual:

`sudo nixos-rebuild build-vm`

- Tampilkan daftar generasi sistem yang tersedia, serupa dengan daftar menu pada boot loader:

`nixos-rebuild list-generations`
