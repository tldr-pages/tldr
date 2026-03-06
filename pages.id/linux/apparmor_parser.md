# apparmor_parser

> Muat, kompilasi, dan kelola profil keamanan AppArmor.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_apparmor_parser.8>.

- Muat profil ke dalam kernel:

`sudo apparmor_parser {{[-a|--add]}} {{profile_file}}`

- Ganti profil yang sudah ada:

`sudo apparmor_parser {{[-r|--replace]}} {{profile_file}}`

- Hapus profil dari kernel:

`sudo apparmor_parser {{[-R|--remove]}} {{profile_name}}`

- Muat profil dalam mode komplain (mencatat pelanggaran tetapi tidak memblokir):

`sudo apparmor_parser {{[-C|--complain]}} {{[-r|--replace]}} {{path/ke/profil}}`

- Lakukan praproses pada profil (selesaikan include) dan tulis cache biner ke file:

`apparmor_parser {{[-p|--preprocess]}} {{[-o|--ofile]}} {{path/ke/output.cache}} {{[-Q|--skip-kernel-load]}} {{path/ke/profil}}`

- Lakukan praproses dan cetak profil biner ke `stdout` tanpa memuatnya:

`apparmor_parser {{[-p|--preprocess]}} {{[-S|--stdout]}} {{[-Q|--skip-kernel-load]}} {{path/ke/profil}}`

- Ganti profil sambil mengabaikan pembacaan cache:

`sudo apparmor_parser {{[-r|--replace]}} {{[-T|--skip-read-cache]}} {{path/ke/profil}}`

- Ganti profil, bangun ulang cache, dan tulis ke direktori kustom:

`sudo apparmor_parser {{[-r|--replace]}} {{[-W|--write-cache]}} {{[-L|--cache-loc]}} /{{path/ke/cache}} {{path/ke/profil}}`
