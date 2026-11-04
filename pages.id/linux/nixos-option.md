# nixos-option

> Lakukan inspeksi terhadap konfigurasi sistem NixOS.
> Informasi lebih lanjut: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- Tampilkan seluruh subkunci dari suatu kata kunci pengaturan (option key):

`nixos-option {{kata_kunci_pengaturan}}`

- Tampilkan daftar modul kernel yang dimuat saat proses boot:

`nixos-option boot.kernelModules`

- Tampilkan daftar kunci OpenSSH yang diizinkan untuk mewakili suatu pengguna:

`nixos-option users.users.{{pengguna}}.openssh.authorizedKeys.{{keyFiles|keys}}`

- Tampilkan daftar seluruh komputer pembantu pembangun paket piranti lunak (remote builder):

`nixos-option nix.buildMachines`

- Tampilkan daftar seluruh subkunci dari kata kunci (option key) dalam berkas konfigurasi sistem NixOS:

`NIXOS_CONFIG={{jalan/menuju/konfigurasi.nix}} nixos-option {{kata_kunci_pengaturan}}`

- Tampilkan seluruh kunci beserta nilai konfigurasi bagi suatu pengguna secara rekursif:

`nixos-option {{[-r|--recursive]}} users.users.{{pengguna}}`
